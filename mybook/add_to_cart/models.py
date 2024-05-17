from django.db import models
from django.contrib.auth.models import User
from home.models import BookModel
# Create your models here.
class OrderModel(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    description = models.TextField(null = True)
    ordered_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.order_number
    
class OrderDetailModel(models.Model):
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.order