from django.contrib import admin
from .models import CategoryBookModel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
    list_filter = ["category_name"]
    search_fields = ["category_name"]
# Register your models here.
admin.site.register(CategoryBookModel, CategoryAdmin)