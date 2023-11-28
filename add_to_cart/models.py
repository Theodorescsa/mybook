from django.db import models
from django.contrib.auth.models import User
from home.models import BookModel
# Create your models here.
class CartModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    cart = models.ManyToManyField(BookModel)
    
    def __str__(self):
        return self.cart