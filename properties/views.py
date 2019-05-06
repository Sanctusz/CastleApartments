from django.shortcuts import render, get_object_or_404
from properties.models import Properties


# Create your views here.
def index(request):
    context = {
        'properties': Properties.objects.all()
    }
    return render(request, 'properties/index.html', context)

def get_property_by_id(request, id):
    return render(request, 'properties/property_details.html', {
        'property': get_object_or_404(Properties, pk=id)
    })