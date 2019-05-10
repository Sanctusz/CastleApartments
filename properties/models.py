from django.db import models

from agents.models import Agents

class PropertiesDetails(models.Model):
    garden = models.BooleanField(blank=True)
    garage = models.BooleanField(blank=True)
    pets = models.BooleanField(blank=True)
    accessibility = models.BooleanField(blank=True)

class PropertiesAddress(models.Model):
    streetName = models.CharField(max_length=999)
    houseNumber = models.FloatField() #ToDo change from Float to int
    zipCode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    def __str__(self):
        return '{} {}'.format(self.streetName, self.houseNumber)

class Properties(models.Model):
    type = models.CharField(max_length=255)
    size = models.IntegerField()
    room = models.IntegerField()
    price = models.FloatField()
    yearBuilt = models.IntegerField()
    details = models.ForeignKey(PropertiesDetails, on_delete=models.CASCADE)
    address = models.ForeignKey(PropertiesAddress, on_delete=models.CASCADE)
    description = models.CharField(max_length=999, blank=True)
    status = models.CharField(max_length=255, default='available')
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)

class PropertiesImages(models.Model):
    link = models.CharField(max_length=999)
    text = models.CharField(max_length=255, blank=True)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)

