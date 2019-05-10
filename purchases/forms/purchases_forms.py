from django.forms import ModelForm, widgets
from django import forms
from purchases.models import *
from clients.models import Profile
from clients.forms.profile_form import ProfileForm

class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['id', 'expirationDate']
        widgets = {
            'ccName': widgets.TextInput(attrs={'class': 'form-control'}),
            'ccNumber': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 16, 'pattern': '[0-9]{16}'}),
            'CVC': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 3, 'pattern': '[0-9]{3}'})
        }