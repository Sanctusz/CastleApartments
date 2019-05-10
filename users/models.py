from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_client = models.BooleanField(default=False),
    is_agent = models.BooleanField(default=False)


class ClientProfile(models.Model):
    userClient = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    fname = models.CharField(max_length=255, blank=True)
    mname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=999, blank=True)


class AgentsProfile(models.Model):
    userAgent = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.phone)
