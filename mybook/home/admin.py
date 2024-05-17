from django.contrib import admin
from .models import BookModel
from django import forms
from ckeditor.widgets import CKEditorWidget
# class CkeditorFormAdmin(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorWidget)
#     class Meta():
#         fields = '__all__'
class BookAdmin(admin.ModelAdmin):
    search_fields = ['book_name','author']
    list_display = ['book_name','author','birth']
    list_filter = ["created_at"]
    # form = CkeditorFormAdmin
# Register your models here.
admin.site.register(BookModel, BookAdmin)