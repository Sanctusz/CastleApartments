from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from properties.forms.property_form import PropertyCreateForm, PropertyUpdateForm
from properties.models import Properties, PropertiesImages
from agents.models import Agents

#def search(request):
    #template = 'properties/index.html'

    #query = request.GET.get('q')
    #if query:
        #results = Properties.objects.filter(Q(address__streetName__icontains=query) | Q(type__icontains=query) | Q(description__icontains=query))
    #else:
        #results = Properties.objects.all()
    #context = {
        #'properties': results
    #}
    #return render(request, template, context)


def index(request):
    context = {
        'properties': Properties.objects.all(),
        'agents': Agents.objects.all()
    }
    return render(request, 'properties/index.html', context)

def search(request):
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

        if 'yearBuilt' in request.GET:
            year_built = request.GET['yearBuilt']
            properties = properties.filter(yearBuilt=year_built)

        if 'location' in request.GET:
            properties = properties.filter(address__streetName__icontains='location')

        if 'rooms' in request.GET:
            properties = properties.filter(rooms='rooms')

        if 'size' in request.GET:
            properties = properties.filter(size='size')


        properties = [{
            'firstImage': x.propertiesimages_set.first().link,
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
    return render(request, 'properties/property_details.html',{
        'property':get_object_or_404(Properties, pk=id)
    })
def create_property(request):
    if request.method == 'POST':
        form = PropertyCreateForm(data=request.POST)
        if form.is_valid():
            property.form.save()
            property_image = PropertiesImages(image=request.POST['image'], propeerty=property)
            property_image.save()
            return redirect('property-index')
    else:
        form = PropertyCreateForm()
    return render(request, 'properties/create_property.html',{
        'form': form
    })
def update_property(request,id):
    instance = get_object_or_404(Properties, pk=id)
    if request.method == 'POST':
        form = PropertyUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('property-details', id=id)
    else:
        form = PropertyUpdateForm(instance=instance)
    return render(request,'properties/update_property.html',{
        'form': form,
        'id': id
    })