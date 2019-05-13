from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from properties.forms.property_form import *
from properties.models import *
from agents.models import Agents
from django.http import HttpResponse


def must_be_agent(func):
    # check if user is in agents group
    # if not, return a warning message
    # else, user is permitted
    # @must_be_agent gives permission to agents
    def check_and_call(request, *args, **kwargs):
        user = request.user
        if not (user.groups.filter(name='agents').exists()):
            return HttpResponse("You do not have permission to view this page !", status=403)
        return func(request, *args, **kwargs)

    return check_and_call


def index(request):
    context = {
        'properties': Properties.objects.all(),
        'agents': Agents.objects.all(),
        'property_types': Properties.objects.distinct('type'),
        'property_zipcodes': Properties.objects.distinct('address__zipCode'),
        'property_countries': Properties.objects.distinct('address__country'),
        'property_cities': Properties.objects.distinct('address__city')
    }
    return render(request, 'properties/index.html', context)


def search(request):
    # if 'search filter' in the url get the value
    # then filter the objects with the matching ones
    # then continue, if 'type' in the url...

    template = 'properties/index.html'

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        properties = Properties.objects.filter(description__icontains=search_filter)

        if 'type' in request.GET:
            house_type = request.GET['type']
            properties = properties.filter(type=house_type)

        if 'status' in request.GET:
            status = request.GET['status']
            properties = properties.filter(status=status)

        if 'city' in request.GET:
            city = request.GET['city']
            properties = properties.filter(address__city__icontains=city)

        if 'country' in request.GET:
            country = request.GET['country']
            properties = properties.filter(address__country__icontains=country)

        if 'room' in request.GET:
            rooms = request.GET['room']
            properties = properties.filter(room__lte=rooms)

        if 'size' in request.GET:
            size = request.GET['size']
            properties = properties.filter(size=size)

        if 'zipcode' in request.GET:
            zipcode = request.GET['zipcode']
            properties = properties.filter(address__zipCode=zipcode)

        if 'price' in request.GET:
            price = request.GET['price']
            properties = properties.filter(price__range=[50000, price])

        if 'garage' in request.GET:
            properties = properties.filter(details__garage=True)

        if 'garden' in request.GET:
            properties = properties.filter(details__garden=True)

        if 'accessibility' in request.GET:
            properties = properties.filter(details__accessibility=True)

        if 'pets' in request.GET:
            properties = properties.filter(details__pets=True)

        properties = [{
            'id': x.id,
            'firstImage': x.propertiesimages_set.first().link,
            'altText': x.propertiesimages_set.first().text,
            'price': x.price,
            'streetName': x.address.streetName,
            'houseNumber': x.address.houseNumber,
            'city': x.address.city,
            'country': x.address.country,
            'zipCode': x.address.zipCode,
            'size': x.size,
            'room': x.room,
            'yearBuilt': x.yearBuilt,
            'status': x.status,
            'type': x.type
        } for x in properties]

        return JsonResponse({'data': properties})

    context = {'properties': Properties.objects.all().order_by('address__streetName')}
    return render(request, template, context)


def get_property_by_id(request, id):
    is_agent = request.user.groups.filter(name="agents").exists()
    return render(request, 'properties/property_details.html', {
        'property': get_object_or_404(Properties, pk=id),
        'is_agent': is_agent
    })


def create_property(request):
    if request.method == 'POST':
        propForm = PropertyCreateForm(data=request.POST)
        propAddressForm = PropertyAddressCreateForm(data=request.POST)
        propDetailsForm = PropertyDetailsCreateForm(data=request.POST)
        propImagesForm = PropertyImagesCreateForm(data=request.POST)
        if (propAddressForm.is_valid()
                and propDetailsForm.is_valid()):
            propAddress = propAddressForm.save()
            propDetails = propDetailsForm.save()
            prop = propForm.save(commit=False)
            prop.address = propAddress
            prop.details = propDetails
            if (propForm.is_valid()):
                prop.save()
                propImages = propImagesForm.save(commit=False)
                propImages.property = prop
                if (propImagesForm.is_valid()):
                    propImages.save()
                    return redirect('index')
    else:
        context = {
            'propertyForm': PropertyCreateForm(),
            'propertyAddressForm': PropertyAddressCreateForm(),
            'propertyDetailsForm': PropertyDetailsCreateForm(),
            'propertyImagesForm': PropertyImagesCreateForm()
        }
        return render(request, 'properties/create_property.html', context)


# only agents're allowed to update properties
@must_be_agent
def update_property(request, id):
    instance = get_object_or_404(Properties, pk=id)
    if request.method == 'POST':
        form = PropertyUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('property-details', id=id)
    else:
        form = PropertyUpdateForm(instance=instance)
    return render(request, 'properties/update_property.html', {
        'form': form,
        'id': id
    })
