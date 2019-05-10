from django.urls import include, path
from . import views
import clients



urlpatterns = [
    path('', views.index, name="user-index"),
    path('accounts/',include('django.contrib.auth.urls')),
  #  path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/agents', views.AgentSignUpView.as_view(), name="agents_signup"),
    path('accounts/signup/clients', views.ClientSignUpView.as_view(), name="clients_signup"),

]
