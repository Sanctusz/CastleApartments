from django.shortcuts import render, get_object_or_404
from agents.models import Agents

def index(request):
    context = {
        'agents': Agents.objects.all()
    }
    return render(request, 'agents/index.html', context)

def about(request):
    context = {
        'agents': Agents.objects.all()
    }
    return render(request, 'about.html', context)

def get_agent_by_id(request, id):
    return render(request, 'agents/agent_details.html', {
        'agent': get_object_or_404(Agents, pk=id)
    })