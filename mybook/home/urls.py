from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
   path('',views.home,name = 'home'),
   path('detail/<int:id>/',views.detail,name = 'detail'),
   path('add/',views.add,name = 'add'),
   path('edit/<int:id>/',views.edit,name = 'edit'),
   path('delete/<int:id>/',views.delete,name = 'delete'),
   path('save_book/<int:id>/', views.save_book, name='save_book'),
   path('yourbook/',views.yourbook,name = 'yourbook'),
   path('add_to_cart/<int:id>/',views.add_to_cart,name = 'add_to_cart'),
   path('buynow/<int:id>/',views.buynow,name = 'buynow'),
   
   path('raing/<int:id>/', views.rating, name='rating'),
   path('get_post_api/', views.get_post_api, name="get_post_api"),
]