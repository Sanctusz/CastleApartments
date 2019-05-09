from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="properties-index"),
    path('search/', views.search, name="properties-search"),
    path('<int:id>', views.get_property_by_id, name='property-details'),
    path('create_property', views.create_property,name='create_property'),
    path('update_candy/<int:id>', views.update_property, name='update_candy')
    #path('search/', views.search, name="properties-search")
]