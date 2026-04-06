from django.urls import path
from .views import *

urlpatterns = [
    path('purchase_add/',purchase_add, name = 'purchase_add')
]
