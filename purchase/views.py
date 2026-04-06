from django.shortcuts import render
from django.shortcuts import render, redirect
from customer.models import Customer
from policies.models import Policy
from .models import CustomerPolicyPurchase
from django.contrib import messages
from datetime import datetime, timedelta

def purchase_add(request):
    try:
        customers = Customer.objects.all()
        policies = Policy.objects.all()
        if request.method == "POST":
            customer_id = request.POST.get("customer")
            policy_id = request.POST.get("policy")
            premium_paid = request.POST.get("premium_paid")
            
            customer = Customer.objects.get(id=customer_id)
            policy = Policy.objects.get(id = policy_id)
            expire_date = datetime.today() + timedelta(days=policy.duration_month * 30)
            
            CustomerPolicyPurchase.objects.create(customer=customer, policy=policy,premium_paid=premium_paid, expire_date=expire_date)
            messages.success(request, "Policy Purchased Successfully")
            return redirect("purchase_list")

        return render(request, "purchase/purchase_form.html", {
            
            
            "customers": customers,
            "policies": policies
        })  

        
    
    except Exception as e:
        print("Policy Purchased Error:", e)
        return render(request, "purchase/purchase_form.html", {
            "error": "Something went wrong"
        })
        

# Create your views here.
