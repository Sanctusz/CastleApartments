from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from properties.forms.property_form import *
from properties.forms.send_email import ContactForm
from properties.models import *
from agents.models import Agents
from django.http import HttpResponse
from clients.views import add_to_recently_viewed
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

def must_be_agent(func):
    # check if user is in agents group
    # if not, return a warning message
    # else, user is permitted
    # @must_be_agent gives permission to agents
    def check_and_call(request, *args, **kwargs):
        user = request.user
        if not (user.groups.filter(name='agents').exists()):
            messages.error(request, "401 Unauthorized!")
            return redirect('index')
        return func(request, *args, **kwargs)
    return check_and_call


def index(request):
    is_agent = request.user.groups.filter(name="agents").exists()
    context = {
        'properties': Properties.objects.all(),
        'agents': Agents.objects.all(),
        'property_types': Properties.objects.distinct('type'),
        'property_zipcodes': Properties.objects.distinct('address__zipCode'),
        'property_countries': Properties.objects.distinct('address__country'),
        'property_cities': Properties.objects.distinct('address__city'),
        'is_agent': is_agent
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

        if 'rooms' in request.GET:
            rooms = request.GET['rooms']
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

        if 'orderbyname' in request.GET:
            properties = properties.order_by('address__streetName')

        if 'orderbyprice' in request.GET:
            properties = properties.order_by('price')

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
            'rooms': x.rooms,
            'yearBuilt': x.yearBuilt,
            'status': x.status,
            'type': x.type
        } for x in properties]

        return JsonResponse({'data': properties})

    context = {'properties': Properties.objects.all()}
    return render(request, template, context)


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
        return form
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['castle_apartments@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return successView(request)

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def get_property_by_id(request, id):
    is_agent = request.user.groups.filter(name="agents").exists()
    email = emailView(request)
    success = successView(request)

    if request.user.is_authenticated:
        add_to_recently_viewed(request, id)
    return render(request, 'properties/property_details.html', {
        'property': get_object_or_404(Properties, pk=id),
        'is_agent': is_agent,
        'email': email,
        'success': success
    })


def order_property_by_name(request):
    template = 'properties/index.html'
    properties_name = {'properties': Properties.objects.all().order_by('address__properties')}
    return render(request, template, properties_name)


@must_be_agent
def create_property(request):
    is_agent = request.user.groups.filter(name="agents").exists()
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
                    messages.success(request, 'Property created successfully')
                    return redirect('property-details', prop.id)
                else:
                    messages.error(request, 'Property cannot be created. Please try again.')
    else:
        context = {
            'propertyForm': PropertyCreateForm(),
            'propertyAddressForm': PropertyAddressCreateForm(),
            'propertyDetailsForm': PropertyDetailsCreateForm(),
            'propertyImagesForm': PropertyImagesCreateForm(),
            'is_agent': is_agent
        }
        return render(request, 'properties/create_property.html', context)


@must_be_agent
def update_property(request, id):
    is_agent = request.user.groups.filter(name="agents").exists()
    prop = Properties.objects.filter(pk=id).first()
    details = prop.details
    address = prop.address
    image = PropertiesImages.objects.filter(property=id).first()
    if request.method == 'POST':
        propForm = PropertyUpdateForm(instance=prop, data=request.POST)
        propAddressForm = PropertyAddressUpdateForm(instance=address, data=request.POST)
        propDetailsForm = PropertyDetailsUpdateForm(instance=details, data=request.POST)
        propMainImageForm = PropertyImagesUpdateForm(instance=image, data=request.POST)
        if (propAddressForm.is_valid()
                and propDetailsForm.is_valid()):
            propAddress = propAddressForm.save()
            propDetails = propDetailsForm.save()
            prop = propForm.save(commit=False)
            prop.address = propAddress
            prop.details = propDetails
            if (propForm.is_valid()):
                prop.save()
                propImages = propMainImageForm.save(commit=False)
                propImages.property = prop
                if (propMainImageForm.is_valid()):
                    propImages.save()
                    messages.success(request, 'Property updated successfully.')
                    return redirect('property-details', id=id)
        else:
            return messages.error(request, 'Property cannot be updated. Please try again.')
    else:
        context = {
            'propertyForm': PropertyUpdateForm(instance=prop),
            'propertyAddressForm': PropertyAddressUpdateForm(instance=address),
            'propertyDetailsForm': PropertyDetailsUpdateForm(instance=details),
            'propertyImagesForm': PropertyImagesUpdateForm(instance=image),
            'is_agent': is_agent
        }
        return render(request, 'properties/update_property.html', context)
