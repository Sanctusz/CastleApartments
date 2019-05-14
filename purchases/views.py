from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from purchases.forms.purchases_forms import *



@login_required()
def get_contact_info(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        property_obj = get_object_or_404(Properties, pk=id)
        cinfoForm = ProfileForm(instance=profile, data=request.POST)
        profile = cinfoForm.save(commit=False)
        profile.user = request.user

        if cinfoForm.is_valid():
            profile.save()
            cinfo = cinfoForm.save()
            return redirect("card_info", property_obj.id,)

    context = {
        'property': get_object_or_404(Properties, pk=id),
        'profileForm': ProfileForm(instance=profile),
    }
    return render(request, 'purchases/contact_info.html', context)


@login_required()
def get_card_info(request, id, cinfo):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        property_obj = get_object_or_404(Properties, pk=id)
        ccForm = CreditCardForm(data=request.POST)
        profile.user = request.user
        if ccForm.is_valid():
            ccForm.save()
            return redirect("confirm_purchase", property_obj.id)

    context = {
        'property': get_object_or_404(Properties, pk=id),
        'creditCardForm': CreditCardForm(),
    }
    return render(request, 'purchases/card_info.html', context)


@login_required()
def confirm_purchase(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        property_obj = get_object_or_404(Properties, pk=id)
        agent_obj = get_object_or_404(Agents, pk=property_obj.agent.id)
        purchaseForm = PurchaseForm(data=request.POST)
        profile.user = request.user

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
            return redirect('index')
    context = {
        'property': get_object_or_404(Properties, pk=id),
        'purchaseForm': PurchaseForm()
    }
    return render(request, 'purchases/confirm_purchase.html', context)


#
# @login_required()
# def purchase_property(request, id):
#     profile = Profile.objects.filter(user=request.user).first()
#     if request.method == 'POST':
#         property_obj = get_object_or_404(Properties, pk=id)
#         agent_obj = get_object_or_404(Agents, pk=property_obj.agent.id)
#
#         cinfoForm = ProfileForm(instance=profile, data=request.POST)
#         profile = cinfoForm.save(commit=False)
#         profile.user = request.user
#
#         ccForm = CreditCardForm(data=request.POST)
#         purchaseForm = PurchaseForm(data=request.POST)
#
#         if cinfoForm.is_valid() and ccForm.is_valid():
#             profile.save()
#             cinfo = cinfoForm.save()
#             ccard = ccForm.save()
#             purchase = purchaseForm.save(commit=False)
#             purchase.buyer = cinfo
#             purchase.realtyAgent = agent_obj
#             purchase.property = property_obj
#             purchase.payment = ccard
#             if purchaseForm.is_valid():
#                 purchaseForm.save()
#                 propForm = PropertyForm(data=request.POST, instance=property_obj)
#                 statuschange = propForm.save(commit=False)
#                 statuschange.status = 'sold'
#                 statuschange.save()
#                 return redirect('index')
#     context = {
#         'property': get_object_or_404(Properties, pk=id),
#         'profileForm': ProfileForm(instance=profile),
#         'creditCardForm': CreditCardForm(),
#         'purchaseForm': PurchaseForm()
#     }
#     return render(request, 'purchases/purchase.html', context)


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

