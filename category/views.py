from .models import  CategoryBookModel  # Import your models
from home.models import BookModel
from django.shortcuts import render, redirect
def list(request):
    # category_list = CategoryBookModel.objects.all()
    category_list = CategoryBookModel.objects.get(id=16)
    context = {
        'category_list':category_list
    }

    return render(request, 'category/list.html',context)

