from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from purchases.forms.purchases_forms import *
from django.contrib import messages

@login_required()
def purchase_property(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        property_obj = get_object_or_404(Properties, pk=id)
        agent_obj = get_object_or_404(Agents, pk=property_obj.agent.id)

        cinfoForm = ProfileForm(instance=profile, data=request.POST)
        profile = cinfoForm.save(commit=False)
        profile.user = request.user

        ccForm = CreditCardForm(data=request.POST)
        purchaseForm = PurchaseForm(data=request.POST)

        if cinfoForm.is_valid() and ccForm.is_valid():
            profile.save()
            cinfo = cinfoForm.save()
            ccard = ccForm.save()
            purchase = purchaseForm.save(commit=False)
            purchase.buyer = cinfo
            purchase.realtyAgent = agent_obj
            purchase.property = property_obj
            purchase.payment = ccard
            if purchaseForm.is_valid():
                purchaseForm.save()
                propForm = PropertyForm(data=request.POST, instance=property_obj)
                statuschange = propForm.save(commit=False)
                statuschange.status = 'sold'
                statuschange.save()
                messages.success(request, "Thank you for your purchase")
                return redirect('index')
            else:
                messages.error(request, "Payment not received. Please try again")
    context = {
        'property': get_object_or_404(Properties, pk=id),
        'profileForm': ProfileForm(instance=profile),
        'creditCardForm': CreditCardForm(),
        'purchaseForm': PurchaseForm()
    }
    return render(request, 'purchases/purchase.html', context)

