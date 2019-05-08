from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, blank=True)
    mname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=999, blank=True)
    #user_contact_info