from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="properties-index"),
    path('search/', views.search, name="properties-search"),
    path('<int:id>', views.get_property_by_id, name='property-details'),
    #path('search/', views.search, name="properties-search")
]