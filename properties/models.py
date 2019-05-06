from django.db import models

from agents.models import Agents


class PropertiesDetails(models.Model):
    garden = models.BooleanField(blank=True)
    garage = models.BooleanField(blank=True)
    pets = models.BooleanField(blank=True)
    accessibility = models.BooleanField(blank=True)

class PropertiesAddress(models.Model):
    streetName = models.CharField(max_length=999)
    houseNumber = models.FloatField()
    zipCode = models.FloatField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Properties(models.Model):
    type = models.CharField(max_length=255)
    size = models.FloatField()
    room = models.FloatField()
    price = models.FloatField()
    yearBuild = models.FloatField()
    details = models.ForeignKey(PropertiesDetails, on_delete=models.CASCADE)
    description = models.CharField(max_length=999, blank=True)
    status = models.CharField(max_length=255)
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)


class PropertiesImages(models.Model):
    image = models.CharField(max_length=999)
    imgeDisc = models.CharField(max_length=255, blank=True)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)

