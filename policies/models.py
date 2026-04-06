from django.db import models

class Policy(models.Model):
    policy_name = models.CharField(max_length = 100)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration_month = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.policy_name
        

# Create your models here.
