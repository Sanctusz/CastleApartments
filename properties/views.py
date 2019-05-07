from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from properties.models import Properties

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


#def index(request):
    #context = {
        #'properties': Properties.objects.all()
    #}
    #return render(request, 'properties/index.html', context)

def index(request):
    template = 'properties/index.html'

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        properties = [ {
            'id': 'x.id',
            'address': 'x.address',
            'description': 'x.description',
            'firstImage': 'x.propertyimage_set.first().image',
        } for x in Properties.objects.filter(address__streetName__icontains=search_filter)]
        return JsonResponse({{ 'data': properties} })

    context = {'properties': Properties.objects.all().order_by('address__streetName')}
    return render(request, template, context)
