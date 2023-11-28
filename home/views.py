from django.shortcuts import render, redirect, HttpResponse
from .models import BookModel
from category.models import CategoryBookModel
from .forms import BookForms, BookModelForms
from django.db.models import Q
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from customer.models import CustomerModel
from user_book.models import Booksave
from django.contrib.auth.models import User
from add_to_cart.models import CartModel
# Create your views here.

def is_superuser(user):
    return user.is_authenticated and user.is_superuser
# @login_required(login_url=settings.LOGIN_URL)
def home(request):
    list_book = BookModel.objects.all()
    keyword = request.GET.get("keyword")
    sort = request.GET.get("sort")
    type = request.GET.get("type")
    page = request.GET.get('page',1)
    limit = 16
    if type:
        list_book = BookModel.objects.filter(category_name__category_name = type)
        
    

    if sort not in ["birth","-birth","book_name"]:
        sort = settings.DEFAULT_SORT
    else:
        list_book = BookModel.objects.all().order_by(sort)
    if keyword:
        list_book = BookModel.objects.filter(
            Q(book_name__icontains = keyword)
            | Q(arthur__icontains = keyword)
            
        )
    
    # if type_book not in ['']
    #paginator
    book_list_paging = Paginator(list_book,limit)
    try:
        book_list_paging = book_list_paging.get_page(page)
    except PageNotAnInteger:
        book_list_paging = book_list_paging.get_page(1)
    except EmptyPage:
        book_list_paging = book_list_paging.get_page(book_list_paging.num_pages)
    context = {
        'list_book':book_list_paging,
        'keyword':keyword if keyword else ""
    }

    return render(request,'home/home.html',context)
@login_required(login_url=settings.LOGIN_URL)
def detail(request,id):
    detail = BookModel.objects.get(id=id)
    context = {
        'detail':detail,
    }
    return render(request,'home/detail.html',context)
@user_passes_test(is_superuser)
def add(request):
    if request.method == 'POST':
        form = BookModelForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = BookModelForms()

    context = {
        'form': form
    }
    return render(request, 'home/add.html', context)



    
@user_passes_test(is_superuser)
def edit(request,id):
    model = BookModel.objects.get(id=id)
    form = BookModelForms(instance=model)
    context = {
        'form':form
    }
    if request.method == "POST":
        form = BookModelForms(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('home:detail',id)
        
    return render(request,'home/edit.html',context)
@user_passes_test(is_superuser)
def delete(request,id):
    model = BookModel.objects.get(id=id)
    model.delete()
    return redirect('home:home')




def save_book(request, id):
    book = BookModel.objects.get(id=id)
    
    # Assuming you have a UserProfile associated with the current user
    user_book, created = Booksave.objects.get_or_create(user=request.user)
    user_book.saved_books.add(book)
    
    return HttpResponse('Success')

def yourbook(request):
    user = User.objects.get(username=request.user.username)
    booksave_object, created = Booksave.objects.get_or_create(user=user)
    saved_books = booksave_object.saved_books.all() 
    context = {
        'book_save':saved_books,
    }
    
    return render(request,'home/yourbook.html',context)

def add_to_cart(request,id):
    book = BookModel.objects.get(id=id)
    user_cart,created = CartModel.objects.get_or_create(user=request.user)
    user_cart.cart.add(book)
    return HttpResponse("Add success")
def cart(request):
    user = User.objects.get(username=request.user.username)
    cart_user = CartModel.objects.get(user=user)
    cart = cart_user.cart.all()
    context = {
        'cart':cart,
    }
    return render(request,'home/cart.html',context)