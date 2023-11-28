from django.db import models
# from home.models import BookModel
# Create your models here.
class CategoryBookModel(models.Model):
    # category_id = models.ForeignKey(BookModel, on_delete=models.PROTECT,null=True)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name