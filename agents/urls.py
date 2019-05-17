from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.get_agent_by_id, name='agent-details')
]
