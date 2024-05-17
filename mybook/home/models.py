from django.db import models
from category.models import CategoryBookModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class BookModel(models.Model):
    category_name = models.ManyToManyField(CategoryBookModel)    
    # category_name = models.ForeignKey(CategoryBookModel,on_delete=models.PROTECT,null = True)
    book_name = models.CharField(max_length=500, null = False)
    quantity_page = models.IntegerField(null = False)
    author = models.CharField(max_length=100, null = True)
    price = models.IntegerField(null=False)
    birth = models.DateField()
    link_image = models.ImageField(null = True,upload_to='images/')
    # description = models.TextField(default=False)
    description = RichTextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    color_card = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.book_name