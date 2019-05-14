from django.contrib.auth.models import User
from django.db import models
from properties.models import Properties


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, blank=True)
    mname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=999, blank=True)
    # user_contact_info
    SSN = models.CharField(max_length=10, blank=True)
    streetName = models.CharField(max_length=999, blank=True)
    houseNumber = models.IntegerField(blank=True, null=True)
    zipCode = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)

class RecentlyViewed(models.Model):
    #ToDo Create the function that manipulates this. So that everytime a property is clicked we should send it to that function
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
