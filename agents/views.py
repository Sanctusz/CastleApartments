from django.shortcuts import render
from agents.models import Agents



def index(request):
    context = {
        'agents': Agents.objects.all()
    }
    return render(request, 'agents/index.html', context)
