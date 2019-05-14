from django.db import models
from properties.models import *
from agents.models import *
from clients.models import *
from django.utils.timezone import now


class CreditCard(models.Model):
    ccName = models.CharField(max_length=255)
    ccNumber = models.CharField(max_length=16)
    CVC = models.CharField(max_length=3)
    expirationDate = models.CharField(max_length=5)


class Purchases(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    realtyAgent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    payment = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
