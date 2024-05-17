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
from add_to_cart.models import OrderModel,OrderDetailModel
from rating.models import RatingModel
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from .serializers import BookSerializers
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
            | Q(author__icontains = keyword)
            
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
    if request.user.username:
        user = User.objects.get(username = request.user.username)
        orders = OrderModel.objects.filter(
            customer = user
        )
        total = len(orders)
    else:
        total = ""
    context = {
        'total':total,
        'list_book':book_list_paging,
        'keyword':keyword if keyword else ""
    }

    return render(request,'home/home.html',context)
@login_required(login_url=settings.LOGIN_URL)
def detail(request,id):
    
    detail = BookModel.objects.get(id=id)
    rating = RatingModel.objects.filter(book = detail)
    total_point = 0
    for i in range(len(rating)):
        total_point += rating[i].point
    if rating.count() == 0:
        average_point = 5
    else:
        average_point = total_point/(rating.count())
    print(rating.count())
    context = {
        'average_point':average_point,
        'detail':detail,
        'rating':rating,
        
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
def delete(request, id):
    model = get_object_or_404(BookModel, id=id)
    
    # ratings = RatingModel.objects.filter(book=model)
    
    model.delete()
    
    # ratings.delete()
    
    return redirect('home:home')

@login_required(login_url=settings.LOGIN_URL)
def save_book(request, id):
    book = BookModel.objects.get(id=id)
    
    # Assuming you have a UserProfile associated with the current user
    user_book, created = Booksave.objects.get_or_create(user=request.user)
    user_book.saved_books.add(book)
    
    return redirect("home:yourbook")

@login_required(login_url=settings.LOGIN_URL)
def yourbook(request):
    user = User.objects.get(username=request.user.username)
    booksave_object, created = Booksave.objects.get_or_create(user=user)
    saved_books = booksave_object.saved_books.all() 
    context = {
        'book_save':saved_books,
    }

    return render(request,'home/yourbook.html',context)

@login_required(login_url=settings.LOGIN_URL)
def add_to_cart(request,id):
    if request.method == "POST":
        customer = User.objects.get(username=request.user.username)

        order, created = OrderModel.objects.get_or_create(
            status = 0,
            customer = customer,
        )
        book = BookModel.objects.get(id=id)
            # order_detail
        try:
            order_detail = OrderDetailModel.objects.get(
                order=order,
                book = book
            )
        except OrderDetailModel.DoesNotExist:
            order_detail = OrderDetailModel.objects.create(
                order = order,
                book = book,
                price = book.price,
                quantity = 0
            )
        order_detail.quantity = order_detail.quantity + 1 if order_detail.quantity else 1
        order_detail.price = book.price
        
        order_detail.save() 
    context = {
        
    }
    return HttpResponse("add success")
    # return render(request,'home/detail.html',context)
    
def rating(request, id):
    point = request.POST.get('point')
    comment = request.POST.get('comment')
    point = int(point)
    user = User.objects.get(username=request.user.username)
    book = get_object_or_404(BookModel, id=id)

    # Kiểm tra xem đã tồn tại đánh giá của người dùng cho cuốn sách chưa
    rating_instance, created = RatingModel.objects.get_or_create(
        user=user,
        book=book,
        comment=comment,
        defaults={'point': point}  # Giá trị mặc định nếu tạo mới
    )

    if not created:
        # Nếu đánh giá đã tồn tại, thì cập nhật giá trị point
        rating_instance.point = point
        rating_instance.save()
    return redirect("home:detail",id)
@api_view(['GET','POST'])
def get_post_api(request):
    if request.method == "GET":
        model = BookModel.objects.all()
        serializer = BookSerializers(model,many = True)
        return Response(serializer.data)