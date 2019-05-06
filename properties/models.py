from django.db import models

# Create your models here.

class PropertyAddress(models.Model):
    streetName= models.CharField(max_length=255)
    houseNr = models.IntegerField(default=None)
    zipCode = models.IntegerField(default=None)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class PropertiesImage(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class PropertyDetails(models.Model):
    garden = models.BooleanField(default=None)
    garage = models.BooleanField(default=None)
    petAllowed = models.BooleanField(default=None)
    Accessibility = models.BooleanField(default=None)

class Properties(models.Model):
    type = models.CharField(max_length=255, default=None)
    size = models.IntegerField(default=None)
    room = models.IntegerField(default=None)
    price = models.FloatField(default=None)
    year_built = models.IntegerField(blank=True,default=None)
    description = models.CharField(max_length=999, blank=True, null=True, default=None)
    details = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE, default=None)
    address = models.ForeignKey(PropertyAddress, on_delete=models.CASCADE, default=None)
