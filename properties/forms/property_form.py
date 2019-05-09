from django.forms import ModelForm, widgets
from django import forms
from properties.models import Properties

class PropertyUpdateForm(ModelForm):
    class Meta:
        model = Properties
        exclude = ['id']
        widgets = {
            'type': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'room': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'yearBuilt': widgets.TextInput(attrs={'class': 'form-control'}),
            'details': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'status': widgets.Select(attrs={'class': 'form-control'}),
            'agent': widgets.TextInput(attrs={'class': 'form-control'}),
            }


class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    class Meta:
        model = Properties
        exclude = ['id', 'image']
        widgets = {
            'type': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'room': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'yearBuilt': widgets.TextInput(attrs={'class': 'form-control'}),
            'details': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'status': widgets.Select(attrs={'class': 'form-control'}),
            'agent': widgets.TextInput(attrs={'class': 'form-control'}),
        }


    #TODO Check what kind of text input class we are going to be using for creaing new property.Via bootstrap

