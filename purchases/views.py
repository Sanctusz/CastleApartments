from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from properties.forms.property_form import PropertyUpdateForm
from purchases.forms.purchases_forms import *


@login_required()
def purchase_property(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        property_obj = get_object_or_404(Properties, pk=id)
        agent_obj = get_object_or_404(Agents, pk=property_obj.agent.id)
        cinfoForm = ProfileForm(instance=profile, data=request.POST)
        cinfoForm.save(commit=False)
        cinfoForm.user = request.user
        ccForm = CreditCardForm(data=request.POST)
        purchaseForm = PurchaseForm(data=request.POST)

        if cinfoForm.is_valid() and ccForm.is_valid():
            cinfo = cinfoForm.save()
            ccard = ccForm.save()
            purchase = purchaseForm.save(commit=False)
            purchase.buyer = cinfo
            purchase.realtyAgent = agent_obj
            purchase.property = property_obj
            purchase.payment = ccard
            if purchaseForm.is_valid():
                purchaseForm.save()
                #CHANGE STATUS
                propForm = PropertyUpdateForm(data=request.POST, instance=property_obj)
                statuschange = propForm.save(commit=False)
                statuschange.status = 'sold'
                statuschange.save()
                return redirect('index')
    context = {
        'property': get_object_or_404(Properties, pk=id),
        'profileForm': ProfileForm(instance=profile),
        'creditCardForm': CreditCardForm(),
        'purchaseForm': PurchaseForm()
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