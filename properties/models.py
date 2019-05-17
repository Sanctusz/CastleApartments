from django.db import models
from agents.models import Agents
from django.core.validators import MinValueValidator


class PropertiesDetails(models.Model):
    garden = models.BooleanField(blank=True)
    garage = models.BooleanField(blank=True)
    pets = models.BooleanField(blank=True)
    accessibility = models.BooleanField(blank=True)


class PropertiesAddress(models.Model):
    streetName = models.CharField(max_length=999)
    houseNumber = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.streetName, self.houseNumber)


class Properties(models.Model):
    type = models.CharField(max_length=255)
    size = models.IntegerField(validators=[MinValueValidator(1)])
    rooms = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(50000)])
    yearBuilt = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=999, blank=True)
    status = models.CharField(max_length=255, default='available')
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    address = models.ForeignKey(PropertiesAddress, on_delete=models.CASCADE)
    details = models.ForeignKey(PropertiesDetails, on_delete=models.CASCADE)


class PropertiesImages(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    link = models.CharField(max_length=999)
    text = models.CharField(max_length=255, blank=True)
