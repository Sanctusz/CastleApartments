from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999, blank=True)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.phone)