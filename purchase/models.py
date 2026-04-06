from django.db import models
from customer.models import Customer
from policies.models import Policy

# Create your models here.
class CustomerPolicyPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete = models.CASCADE)
    
    purchase_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateField()
    premium_paid = models.DecimalField(max_digits=10, decimal_places=2)
    
    STATUS_CHOICE = (
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('CANCELLED', 'Cancelled')
    )
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='ACTIVE')
    def __str__(self):
        return f"{self.customer} - {self.policy}"