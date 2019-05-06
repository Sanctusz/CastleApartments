from django.shortcuts import render
from properties.models import Properties


# Create your views here.
def index(request):
    context = {
        'properties': Properties.objects.all(),
    }
    return render(request, 'properties/index.html', context)
