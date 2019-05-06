from django.shortcuts import render
from django.db.models import Q
from properties.models import Properties

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
        'properties': Properties.objects.all()
    }
    return render(request, 'properties/index.html', context)
