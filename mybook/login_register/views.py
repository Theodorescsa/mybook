from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def login(request):
    user_name = ''
    pass_word = ''
    next = request.GET.get('next')

    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        is_auth = authenticate(username = user_name,password = pass_word)
        if is_auth:
            auth_login(request, is_auth)
            if next:
                return redirect(next)
            return redirect('home:home')
    
    return render(request,"login_register/loginform.html")


