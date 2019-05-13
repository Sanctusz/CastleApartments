from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from clients.models import Profile
from clients.forms.profile_form import ProfileForm

# Create your views here.
def index(request):
    return render(request, 'clients/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients-login')
    return render(request, 'clients/register.html', {
        'form': UserCreationForm()
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

def addToRecentlyViewed(request, id):
    #ToDo Finish!!!!
    user = request.user
    if (user.groups.filter(name='clients').exists()):
