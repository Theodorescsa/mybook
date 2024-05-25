from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'partner'
urlpatterns = [
    path('',views.partner_list,name = "list"),
    path('api/',views.list_api,name = 'list_api'),
    path('<int:id>/',views.partner_detail,name = "detail"),  
]
