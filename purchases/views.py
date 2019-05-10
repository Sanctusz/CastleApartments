from django.shortcuts import render, get_object_or_404, redirect
from properties.forms.property_form import *
from properties.models import *
from agents.models import Agents
from clients.models import Profile
from purchases.forms.purchases_forms import *


def purchase_property(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    context = {
        'property': get_object_or_404(Properties, pk=id),
        'profileForm': ProfileForm(instance=profile),
        'creditCardForm': CreditCardForm()
    }
    return render(request, 'purchases/purchase.html', context)


'''
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

def purchase_property(request, id):
    # prop = Properties.objects.get(pk=id)
    if request.method=="PATCH":
        prop = get_object_or_404(Properties, id=id)
        if prop.status == 'available':
            prop.status = "sold"
            prop.save()
'''