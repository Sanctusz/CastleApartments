from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from properties.models import Properties
from agents.models import Agents

def search(request):
    template = 'properties/index.html'

    query = request.GET.get('q')
    if query:
        results = Properties.objects.filter(Q(address__streetName__icontains=query) | Q(type__icontains=query) | Q(description__icontains=query))
    else:
        results = Properties.objects.all()
    context = {
        'properties': results
    }
    return render(request, template, context)


def index(request):
    context = {
        'properties': Properties.objects.all(),
        'agents': Agents.objects.all()
    }
    return render(request, 'properties/index.html', context)

def get_property_by_id(request, id):
    return render(request, 'properties/property_details.html', {
        'property': get_object_or_404(Properties, pk=id)
    })
