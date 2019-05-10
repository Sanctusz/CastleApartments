from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from users.models import ClientProfile,AgentsProfile
from users.forms import AgentSignUpForm
from users.forms import ClientSignUpForm

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def SignUpView(request):
    return render(request, 'users/register.html')


class AgentSignUpView(CreateView):
    model = AgentsProfile
    form_class = AgentSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('properties-index')

class ClientSignUpView(CreateView):
    model = ClientProfile
    form_class = ClientSignUpForm
    template_name = 'users/register.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:profile')
