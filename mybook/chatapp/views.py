from django.shortcuts import render
from .models import ChatModel, MessageModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, "chatapp/index.html")
@login_required(login_url=settings.LOGIN_URL)
def room(request, room_name):
    room_chat,created = ChatModel.objects.get_or_create(room_name = room_name)
    user = User.objects.get(username = request.user.username)
    list_room_chat = MessageModel.objects.filter(
        user = user
    )
    messages = MessageModel.objects.filter(room_name = room_chat)
    context = {
        "room_name": room_name,
        "list_room":list_room_chat,
        "messages":messages
    }
    return render(request, "chatapp/room.html", context)
@login_required(login_url=settings.LOGIN_URL)
def list_room(request):
    user = User.objects.get(username = request.user.username)
    list_room_chat = MessageModel.objects.filter(
        user = user
    )
    context = {
        "list_room":list_room_chat,
        
    }
    return render(request, "chatapp/listroom.html", context)
