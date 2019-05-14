from django.forms import ModelForm, widgets
from clients.models import Profile, RecentlyViewed


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'fname': widgets.TextInput(attrs={'class': 'form-control'}),
            'mname': widgets.TextInput(attrs={'class': 'form-control'}),
            'lname': widgets.TextInput(attrs={'class': 'form-control'})
        }

class RecentlyViewedForm(ModelForm):
    class Meta:
        model = RecentlyViewed
        exclude = ['user', 'property', 'time']
