from django.contrib import admin
from .models import OrderModel, OrderDetailModel
# Register your models here.
admin.site.register(OrderModel)
admin.site.register(OrderDetailModel)
