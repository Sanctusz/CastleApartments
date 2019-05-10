from django.forms import ModelForm, widgets
from django import forms
from properties.models import *


DETAILS_CHOICES = (
    ('garden', 'Garden'),
    ('garage', 'Garage'),
    ('accessability', 'Accessability'),
    ('pets', 'Pets Allowed')
)
houseTypes = (
    ('house', 'House'),
    ('apartment', 'Apartment'),
    ('castle', 'Castle')
)

class PropertyUpdateForm(ModelForm):
    class Meta:
        widgets = {
            'type': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'room': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'yearBuilt': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'status': widgets.Select(attrs={'class': 'form-control'}),
            'agent': widgets.TextInput(attrs={'class': 'form-control'}),
            }
        model = Properties
        exclude = ['id']


class PropertyImagesCreateForm(ModelForm):
    class Meta:
        labels = {'link': 'Image URL:', 'text': 'Image alt-text:'}
        model = PropertiesImages
        exclude = ['property']
        widgets = {
            'link': widgets.TextInput(attrs={'class': 'form-control'}),
            'text': widgets.TextInput(attrs={'class': 'form-control'})
        }


class PropertyDetailsCreateForm(ModelForm):
    class Meta:
        model = PropertiesDetails
        exclude = ['id']
        widgets = {
            'garden': widgets.CheckboxInput(),
            'garage': widgets.CheckboxInput(),
            'accessibility': widgets.CheckboxInput(),
            'pets': widgets.CheckboxInput()
        }


class PropertyAddressCreateForm(ModelForm):
    class Meta:
        model = PropertiesAddress
        exclude = []
        widgets = {
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class PropertyCreateForm(ModelForm):
    class Meta:
        model = Properties
        exclude = ['id', 'address', 'details', 'status']
        widgets = {
            'type': widgets.Select(attrs={'class': 'form-control'}, choices=houseTypes),
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'room': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'yearBuilt': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'agent': widgets.Select(attrs={'class': 'form-control'})
        }