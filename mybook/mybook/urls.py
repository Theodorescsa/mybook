"""
URL configuration for mybook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('category/',include('category.urls')),
    path('login/',include('login_register.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),    
    path('register/',include('register.urls')),
    path('logout2/',include('logout2.urls')),
    path('partner/',include('partner.urls')),
    path('auth_api/',include('auth_api.urls')),
    path('profile/',include('profile_app.urls')),
    path('cart/',include('cart.urls')),
    path('chatapp/',include('chatapp.urls')),
    
    
    
    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

