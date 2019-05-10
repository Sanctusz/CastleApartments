from django.forms import ModelForm, widgets
from django.db import transaction

from users.models import User, ClientProfile



class ClientSignUpForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id','user']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'fname': widgets.TextInput(attrs={'class': 'form-control'}),
            'mname': widgets.TextInput(attrs={'class': 'form-control'}),
            'lname': widgets.TextInput(attrs={'class': 'form-control'})
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        clientprofile = ClientProfile.objects.create(user=user)
        return user

class AgentSignUpForm(ModelForm):
    model = User
    exclude = ['id','user']
    widgets = {
        'name': widgets.TextInput(attrs={'class': 'form-control'}),
        'email': widgets.TextInput(attrs={'class': 'form-control'}),
        'phone': widgets.TextInput(attrs={'class': 'form-control'}),
        'description': widgets.TextInput(attrs={'class': 'form-control'}),
        'image': widgets.TextInput(attrs={'class': 'form-control'})
    }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_agent = True
        if commit:
            user.save
        return user
