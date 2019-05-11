from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name="agents-index"),
    path('<int:id>', views.get_agent_by_id, name='agent-details')
]