from django.contrib import admin

# Register your models here.

from .models import Properties
from .models import PropertyDetails
from .models import PropertiesImage
from .models import PropertyAddress


admin.site.register(Properties)
admin.site.register(PropertyDetails)
admin.site.register(PropertyAddress)
admin.site.register(PropertiesImage)
