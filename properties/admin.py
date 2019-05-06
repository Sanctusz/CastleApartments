from django.contrib import admin

# Register your models here.

from .models import Properties
from .models import PropertiesDetails
from .models import PropertiesImages
from .models import PropertiesAddress


admin.site.register(Properties)
admin.site.register(PropertiesDetails)
admin.site.register(PropertiesAddress)
admin.site.register(PropertiesImages)
