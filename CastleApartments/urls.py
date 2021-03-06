"""castle_apartments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from CastleApartments import settings
from properties import views as propview
from agents import views as agentview

urlpatterns = [
    path('', propview.index, name='index'),
    path('properties/', include('properties.urls')),
    path('clients/', include('clients.urls')),
    path('agents/', include('agents.urls')),
    path('purchases/', include('purchases.urls')),
    path('admin/', admin.site.urls),
    path('about/', agentview.about, name='about'),
    path('contact/', agentview.contact, name='contact')

]
