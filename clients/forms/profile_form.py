from django.forms import ModelForm, widgets
from clients.models import Profile, RecentlyViewed
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password1': widgets.PasswordInput(attrs={'class': 'form-control'}),
            'password2': widgets.PasswordInput(attrs={'class': 'form-control'})
        }


class fnameRegisterForm(ModelForm):
    class Meta:
        labels = {'fname': 'First Name'}
        help_texts = {'fname': 'Please enter your first name.'}
        model = Profile
        exclude = [
            'id',
            'user',
            'mname',
            'lname',
            'streetName',
            'houseNumber',
            'zipCode',
            'country',
            'city',
            'image',
            'SSN'
        ]
        widgets = {
            'fname': widgets.TextInput(attrs={'class': 'form-control'})
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
        exclude = ['id', 'user']
        widgets = {
            'fname': widgets.TextInput(attrs={'class': 'form-control'}),
            'mname': widgets.TextInput(attrs={'class': 'form-control'}),
            'lname': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'SSN': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{10}'}),
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
        }

class RecentlyViewedForm(ModelForm):
    class Meta:
        model = RecentlyViewed
        exclude = ['user', 'property', 'time']
        

