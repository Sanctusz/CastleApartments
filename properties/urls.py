from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="properties-index"),
    path('search/', views.search, name="properties-search"),
    path('<int:id>', views.get_property_by_id, name='property-details'),
    path('create_property', views.create_property, name='create-property'),
    path('update_property/<int:id>', views.update_property, name='update-property'),
    path('email/', views.emailView, name='email'),
    path('add_images/<int:id>', views.add_images, name='add-images'),
    path('remove_image/<int:prop_id>/<int:image_id>', views.remove_image, name='remove-image')
]
