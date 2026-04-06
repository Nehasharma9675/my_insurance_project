from django.urls import path
from .views import *
 
urlpatterns = [
    path('add/', customer_add, name='customer_add'),
    path('list/', customer_list, name='customer_list'),
    path('edit/<int:id>/', customer_edit , name = 'customer_edit'),
    path('delete/<int:id>/', customer_delete , name = 'customer_delete'),
    
]

