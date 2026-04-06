from django.urls import path
from .views import *
urlpatterns = [
   path('admin/', admin_dashboard, name='admin_dashboard'),
   path('agent/', agent_dashboard, name='agent_dashboard'),
   path('customer/', customer_dashboard, name='customer_dashboard'),
]