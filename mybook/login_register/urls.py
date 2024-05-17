from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'lgr'
urlpatterns = [
    path('',views.login,name = "login"),
]
