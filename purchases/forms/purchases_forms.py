from django import forms
from django.forms import ModelForm, widgets
from purchases.models import *
from clients.models import Profile
from properties.models import Properties
from django_countries.widgets import CountrySelectWidget


class CreditCardForm(ModelForm):
    my_default_errors = {
        'required': 'This field is required',
        'invalid': 'Enter a valid value'
    }
    ccName_help = 'Name of the credit card holder.'
    ccNumber_help = 'Only digits.'
    CVC_help = 'Security Code on the back of the credit card, Only digits.'
    expirationDate_help = 'MM/YY stated on the credit card.'

    ccName = forms.CharField(error_messages=my_default_errors, help_text=ccName_help)
    ccNumber = forms.CharField(error_messages=my_default_errors, help_text=ccNumber_help)
    CVC = forms.CharField(error_messages=my_default_errors, help_text=CVC_help)
    expirationDate = forms.CharField(error_messages=my_default_errors, help_text=expirationDate_help)

    class Meta:
        model = CreditCard
        exclude = ['id']


class ProfileForm(ModelForm):
    class Meta:
        labels = {
            'fname': 'First Name',
            'mname': 'Middle Name',
            'lname': 'Last Name',
            'streetName': 'Street Name',
            'houseNumber': 'House Number',
            'zipCode': 'Zip Code'
        }
        model = Profile
        exclude = ['id', 'user', 'image']
        widgets = {
            'fname': widgets.TextInput(attrs={'class': 'form-control'}),
            'mname': widgets.TextInput(attrs={'class': 'form-control'}),
            'lname': widgets.TextInput(attrs={'class': 'form-control'}),
            'SSN': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{10}'}),
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control'})
        }


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchases
        exclude = ['id', 'buyer', 'realtyAgent', 'property', 'payment', 'date']


class PropertyForm(ModelForm):
    class Meta:
        model = Properties
        exclude = [
            'id',
            'type',
            'size',
            'rooms',
            'price',
            'yearBuilt',
            'address',
            'description',
            'status',
            'agent',
            'details'
        ]
