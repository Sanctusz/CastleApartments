from django.db import models

# Create your models here.
class Agents(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999, blank=True)
    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.phone)