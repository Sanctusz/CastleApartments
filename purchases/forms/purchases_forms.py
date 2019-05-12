from django.forms import ModelForm, widgets
from purchases.models import *
from clients.models import Profile
from properties.models import Properties


class CreditCardForm(ModelForm):
    class Meta:
        labels = {
            'ccName': 'Name on the Credit Card',
            'ccNumber': 'Credit Card Number',
            'CVC': 'CVC',
            'expirationDate': 'Expiration Date'
        }
        model = CreditCard
        exclude = ['id']
        widgets = {
            'ccName': widgets.TextInput(attrs={'class': 'form-control'}),
            'ccNumber': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 16, 'pattern': '[0-9]{16}'}),
            'CVC': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 3, 'pattern': '[0-9]{3}'}),
            'expirationDate': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 5, 'pattern': '[0-9]{5}'})
        }


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
            'houseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
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
            'room',
            'price',
            'yearBuilt',
            'address',
            'description',
            'status',
            'agent',
            'details'
        ]