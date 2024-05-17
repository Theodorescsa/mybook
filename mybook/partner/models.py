from django.db import models

# Create your models here.
class PartnerModel(models.Model):
    name_company = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name_company
    