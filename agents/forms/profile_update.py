from django.forms import ModelForm, widgets
from clients.models import Profile


class ProfileFormUpdate(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'email']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }
