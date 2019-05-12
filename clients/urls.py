from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="clients-register"),
    path('login/', LoginView.as_view(template_name="clients/login.html"), name="clients-login"),
    path('logout/', LogoutView.as_view(next_page="clients-login"), name="clients-logout"),
    path('profile/', views.profile, name='clients-profile')
]