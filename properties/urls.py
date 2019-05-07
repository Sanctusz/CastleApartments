from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="properties-index"),
    path('search/', views.search, name="properties-search")
]