from django.contrib import admin
from .models import Profile
from .models import RecentlyViewed

admin.site.register(RecentlyViewed)
admin.site.register(Profile)
