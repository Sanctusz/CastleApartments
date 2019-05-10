from django.shortcuts import render, get_object_or_404, redirect

from agents.forms.profile_form import ProfileFormUpdate
from agents.models import Agents
from clients.models import Profile
from clients.forms.profile_form import ProfileForm


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

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileFormUpdate(instance=profile, data=request.POST)
        if form.is_valid():
            profile.save()
            return redirect('agent-profile')
    return render(request, 'agent/profile.html', {
        'form': ProfileFormUpdate(instance=profile)
    })

