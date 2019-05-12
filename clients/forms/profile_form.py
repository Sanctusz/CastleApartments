from django.forms import ModelForm, widgets
from clients.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password1': widgets.PasswordInput(),
            'password2': widgets.PasswordInput(attrs={'class': 'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'fname': widgets.TextInput(attrs={'class': 'form-control'}),
            'mname': widgets.TextInput(attrs={'class': 'form-control'}),
            'lname': widgets.TextInput(attrs={'class': 'form-control'}),
            'SSN': widgets.TextInput(attrs={'class': 'form-control', 'max-length': '10', 'pattern': '[0-9]{10}'}),
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.TextInput(attrs={'class': 'form-control', 'max-length': '3', 'pattern': '[0-9]{3}'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
        }
