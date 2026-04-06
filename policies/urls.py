from django.urls import path
from .views import *   
urlpatterns = [
    path('addPolicy/', Policy_add, name='add_policy'),
    path('policyList/', policy_list, name='policy_list'),
    path('policyEdit/<int:id>/', policy_edit , name = 'policy_edit'),
    path('policyDelete/<int:id>/', policy_delete , name = 'policy_delete'),
]