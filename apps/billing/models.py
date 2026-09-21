from django.conf import settings
from django.db import models
class Plan(models.Model):
    name=models.CharField(max_length=80,unique=True); slug=models.SlugField(unique=True); description=models.TextField(blank=True); price=models.DecimalField(max_digits=10,decimal_places=2); currency=models.CharField(max_length=3,default='USD'); interval=models.CharField(max_length=20,default='month'); features=models.JSONField(default=list); is_active=models.BooleanField(default=True)
class Subscription(models.Model):
    STATUS=[('active','Active'),('cancelled','Cancelled'),('expired','Expired'),('pending','Pending')]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='subscriptions'); plan=models.ForeignKey(Plan,on_delete=models.PROTECT); status=models.CharField(max_length=20,choices=STATUS,default='pending'); provider=models.CharField(max_length=50,default='manual'); provider_subscription_id=models.CharField(max_length=255,blank=True); started_at=models.DateTimeField(auto_now_add=True); ends_at=models.DateTimeField(null=True,blank=True); auto_renew=models.BooleanField(default=True)
class Payment(models.Model):
    STATUS=[('pending','Pending'),('paid','Paid'),('failed','Failed'),('refunded','Refunded')]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); plan=models.ForeignKey(Plan,on_delete=models.PROTECT); amount=models.DecimalField(max_digits=10,decimal_places=2); currency=models.CharField(max_length=3,default='USD'); provider=models.CharField(max_length=50); transaction_id=models.CharField(max_length=255,blank=True); status=models.CharField(max_length=20,choices=STATUS,default='pending'); created_at=models.DateTimeField(auto_now_add=True)
