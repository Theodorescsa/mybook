from django.urls import path

from . import views

app_name = "chatapp"
urlpatterns = [
    path("create/", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("", views.list_room, name="list_room"),
    

]