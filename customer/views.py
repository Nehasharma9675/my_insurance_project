from django.shortcuts import redirect, render
import re
from accounts.models import User
import customer
from customer.models import Customer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def customer_add(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        phone = request.POST.get("phone", "").strip()
        city = request.POST.get("city", "").strip()
        state = request.POST.get("state", "").strip()
        kyc_document = request.FILES.get("kyc_document")
        
        # Validation
        errors = {}
        if len(username) < 3:
            errors['username'] = 'Username must be at least 3 characters.'
        password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@!#$%^&*]{6,}$'

        if not re.match(password_pattern, password):
            errors['password'] = 'Password must be 6+ characters with letters and numbers.'
        if len(phone) < 10:
            errors['phone'] = 'Invalid phone number.'
        if not city:
            errors['city'] = 'City is required.'
        if not state:
            errors['state'] = 'State is required.'
        
        if errors:
            return render(request, "customers/customer_form.html", {'errors': errors})
        
        try:
            user = User.objects.create_user(username=username, password=password, role="CUSTOMER")
            customer = Customer.objects.create(user=user, phone=phone, city=city, state=state, kyc_document=kyc_document)
            print("Customer Created:", customer)
            return redirect("customer_list")
        except Exception as e:
            errors['general'] = f'Error creating customer: {str(e)}'
            return render(request, "customers/customer_form.html", {'errors': errors})
    
    return render(request, "customers/customer_form.html")


def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    print("customer", customer)
    if request.method == "POST":
        customer.phone = request.POST.get('phone')
        customer.city  = request.POST.get('city')
        customer.state = request.POST.get('state')
        if request.FILES.get('kyc_document'):
            customer.kyc_document = request.FILES.get('kyc_document')
        customer.save()
        return redirect('customer_list')

    return render(request, 'customers/customer_edit.html', {
        'customer': customer
    })


def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    print("1111111", customer)
    if request.method == "POST":
        customer.delete()
        messages.success(request, "Customer deleted successfully")
    return redirect('customer_list')


def customer_list(request):
    customer_list = Customer.objects.select_related('user').all().order_by('-id')
    print("customer_list", customer_list)
    paginator = Paginator(customer_list,10)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)
    return render(request, 'customers/customers_list.html', {
        'customers': customers
    })


        
   
    
    
