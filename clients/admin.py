from django.contrib import admin


from .models import RecentlyViewed


admin.site.register(RecentlyViewed)
from .models import Profile

admin.site.register(Profile)
