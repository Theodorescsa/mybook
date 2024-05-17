from django.db import models
from django.contrib.auth.models import User
from home.models import BookModel
# Create your models here.
class Booksave(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    saved_books = models.ManyToManyField(BookModel)
    
    def __str__(self) -> str:
        return self.saved_books