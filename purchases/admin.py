from django.contrib import admin

from .models import Purchases
from .models import CreditCard


admin.site.register(Purchases)
admin.site.register(CreditCard)