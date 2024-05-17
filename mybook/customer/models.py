from django.db import models
from django.contrib.auth.models import User
from home.models import BookModel
# Create your models here.

class CustomerModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200,null =True)
    saved_books = models.ManyToManyField(BookModel, blank=True)    
    
    def __str__(self):
        return self.last_name

