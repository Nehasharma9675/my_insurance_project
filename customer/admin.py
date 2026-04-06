from django.contrib import admin
from .models import Customer
admin.site.register(Customer)
def customerAdmin():
       list_display = ('user', 'phone', 'city', 'state')
# Register your models here.
