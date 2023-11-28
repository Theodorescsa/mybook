from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "profile"


urlpatterns = [

    path('',views.profile_app,name = 'profile')

]