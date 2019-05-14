from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>', views.purchase_property, name='purchase'),
    path('<int:id>/contact_info', views.get_contact_info, name='contact_info'),
    path('<int:id>/card_info', views.get_card_info, name='card_info'),
    path('<int:id>/confirm_purchase', views.confirm_purchase, name='confirm_purchase')
]