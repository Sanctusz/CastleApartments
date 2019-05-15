from django.forms import ModelForm, widgets
from properties.models import *

DETAILS_CHOICES = (
    ('garden', 'Garden'),
    ('garage', 'Garage'),
    ('accessability', 'Accessability'),
    ('pets', 'Pets Allowed')
)

homeTypes = (
    ('house', 'House'),
    ('apartment', 'Apartment'),
    ('castle', 'Castle')
)

availability = {
    ('available', 'Available'),
    ('sold', 'Sold')
}


class PropertyUpdateForm(ModelForm):
    class Meta:
        model = Properties
        exclude = ['id', 'address', 'details']
        widgets = {
            'type': widgets.Select(attrs={'class': 'form-control'}, choices=homeTypes),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'yearBuilt': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'status': widgets.Select(attrs={'class': 'form-control'}, choices=availability),
            'agent': widgets.Select(attrs={'class': 'form-control'}),
        }


class PropertyImagesUpdateForm(ModelForm):
    class Meta:
        labels = {'link': 'Image URL:', 'text': 'Image alt-text:'}
        model = PropertiesImages
        exclude = ['property']
        widgets = {
            'link': widgets.TextInput(attrs={'class': 'form-control'}),
            'text': widgets.TextInput(attrs={'class': 'form-control'})
        }


class PropertyDetailsUpdateForm(ModelForm):
    class Meta:
        model = PropertiesDetails
        exclude = ['id']
        widgets = {
            'garden': widgets.CheckboxInput(),
            'garage': widgets.CheckboxInput(),
            'accessibility': widgets.CheckboxInput(),
            'pets': widgets.CheckboxInput()
        }


class PropertyAddressUpdateForm(ModelForm):
    class Meta:
        model = PropertiesAddress
        exclude = ['id']
        widgets = {
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
        }


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
        exclude = ['id']
        widgets = {
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class PropertyCreateForm(ModelForm):
    class Meta:
        model = Properties
        exclude = ['id', 'address', 'details', 'status']
        widgets = {
            'type': widgets.Select(attrs={'class': 'form-control'}, choices=homeTypes),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'yearBuilt': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'agent': widgets.Select(attrs={'class': 'form-control'})
        }
