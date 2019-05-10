from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import ClientSignUpForm
from ..models import User


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'users/register.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:profile')