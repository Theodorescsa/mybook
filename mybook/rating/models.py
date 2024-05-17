from django.db import models
from django.contrib.auth.models import User
from home.models import BookModel
from django.core.validators import MinValueValidator, MaxValueValidator

class RatingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    comment = models.TextField()
    point = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

# Create your models here.
    def __str__(self):
        return self.comment