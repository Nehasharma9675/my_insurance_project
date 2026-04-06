from django.shortcuts import redirect, render
import re
from accounts.models import User
import policies
from policies.models import Policy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

def Policy_add(request):
    try:
        if request.method == "POST":
            policy_name =  request.POST.get("policy_name","").strip()
            premium_amount = request.POST.get("premium_amount","").strip()
            duration_month =  request.POST.get("duration_month","").strip()
            description =  request.POST.get("description","").strip()
            
            if not policy_name or not premium_amount or not duration_month:
                messages.error(request, "Please fill in all required fields.")
                return render(request, "policies/policy_form.html")
            
            premium_amount = float(premium_amount)
            duration_month = int(duration_month)
            
            policy = Policy.objects.create(policy_name=policy_name,premium_amount=premium_amount,duration_month=duration_month,description=description)
            print("Policy Created:", policy)
            return redirect("policy_list")
        return render(request, "policies/policy_form.html")
            
    except Exception as e:
        print("Policy Add Error:", e)
        return render(request, "policies/policy_form.html", {
            "error": "Something went wrong"
        })
        
def policy_list(request):
    policy = Policy.objects.all()
    print("policy", policy)
    paginator = Paginator(policy,10)
    page_number = request.GET.get('page')
    policies = paginator.get_page(page_number)
    return render(request,'policies/policy_list.html', {'policies':policies})

def policy_edit(request,id):
    try:
        policy = get_object_or_404(Policy, id=id)
        if request.method == "POST":
            policy.policy_name =  request.POST.get("policy_name").strip()
            policy.premium_amount = request.POST.get("premium_amount").strip()
            policy.duration_month =  request.POST.get("duration_month").strip()
            policy.description =  request.POST.get("description").strip()
            policy.save()
            return redirect("policy_list")
        return render(request,"policies/policy_edit.html",{"policy":policy})
            
    except Exception as e:
        print("Policy Edit Error:", e)
        return render(request,"policies/policy_edit.html")
    
def policy_delete(request, id):
    try:
        policy = get_object_or_404(Policy, id=id)

        if request.method == "POST":
            policy.delete()
            messages.success(request, "Policy deleted successfully")

    except Exception as e:
        print("Policy Delete Error:", e)
        messages.error(request, "Something went wrong while deleting policy")

   
    return redirect('policy_list')
        
        
        




    
