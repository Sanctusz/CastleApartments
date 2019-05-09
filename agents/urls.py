from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name="agents-index"),
    path('<int:id>', views.get_agent_by_id, name='agent-details'),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="agent-login"),
    path('logout/', LogoutView.as_view(next_page="agent-login"), name="agent-logout")

]