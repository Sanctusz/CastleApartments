from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="agents-index"),
    path('<int:id>', views.get_agent_by_id, name='agent-details')
]
