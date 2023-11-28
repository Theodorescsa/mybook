from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'logout2'
urlpatterns = [
    path('',views.logout2,name = "logout2"),
]
