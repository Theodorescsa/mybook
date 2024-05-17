from django.shortcuts import render, redirect
from add_to_cart.models import OrderModel, OrderDetailModel
from django.contrib.auth.models import User
from home.models import BookModel
from django.contrib.auth.decorators import login_required  
from django.conf import settings
import uuid
# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def cart(request):
 
    user = User.objects.get(username=request.user.username)
    
    order = OrderModel.objects.filter(
        status = 0,
        customer = user
    ).first()
  
    orderdetail = OrderDetailModel.objects.filter(order=order)

    context = {
        'order':order,
        'sss':orderdetail
    }
    return render(request,'cart/cart.html',context)

def ordersuccess(request,id):
    order = OrderModel.objects.get(id=id,status = 0)
    description = request.POST.get('description')

    order.description = description
    order.status = 1
    order.order_number = str(uuid.uuid4())
    order.save()
    context = {
        'order':order,
    }
        
    return render(request,'cart/ordersuccess.html',context)