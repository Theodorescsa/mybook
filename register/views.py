from django.shortcuts import render, redirect
from .forms import RegisterFormModel
# Create your views here.
def register(request):
    form  = RegisterFormModel()
    if request.method == "POST":
        form = RegisterFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lgr:login")
    context = {
        'form':form
    }
    return render(request,'register/register.html',context)