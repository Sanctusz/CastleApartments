from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from properties.models import Properties
from agents.models import Agents

# delete

def index(request):
    context = {
        'properties': Properties.objects.all(),
        'agents': Agents.objects.all()
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
            room = request.GET['room']
            properties = properties.filter(room=room)

        if 'size' in request.GET:
            size = request.GET['size']
            properties = properties.filter(size=size)

        if 'zipcode' in request.GET:
            zipcode = request.GET['zipcode']
            properties = properties.filter(address__zipCode=zipcode)

        if 'price' in request.GET:
            price = request.GET['price']
            properties = properties.filter(price__range=[40000,price])


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
