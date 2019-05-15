from django.shortcuts import render, redirect
from clients.models import Profile
from clients.forms.profile_form import RegisterForm
from clients.forms.profile_form import ProfileForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile created successfully')
            return redirect('clients-login')
        else:
            messages.error(request, 'Registration failed. Please try again')
    return render(request, 'clients/register.html', {
        'form': RegisterForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        profile = form.save(commit=False)
        profile.user = request.user
        if form.is_valid():
            profile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('clients-profile')
        else:
            messages.error(request, 'Update failed. Please try again')
    return render(request, 'clients/profile.html', {
        'form': ProfileForm(instance=profile)
    })
