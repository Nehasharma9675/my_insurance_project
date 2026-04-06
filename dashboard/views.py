from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from accounts.decorators import role_required


@login_required
@role_required('ADMIN')
def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")

@login_required
@role_required('AGENT')
def agent_dashboard(request):
    return HttpResponse("Agent Dashboard")

@login_required
@role_required('CUSTOMER')
def customer_dashboard(request):
    return HttpResponse("Customer Dashboard")
# Create your views here.
