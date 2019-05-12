from django.shortcuts import render, redirect
from clients.models import Profile
from clients.forms.profile_form import ProfileForm, RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients-login')
    return render(request, 'clients/register.html', {
        'form': RegisterForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('clients-profile')
    return render(request, 'clients/profile.html', {
        'form': ProfileForm(instance=profile)
    })