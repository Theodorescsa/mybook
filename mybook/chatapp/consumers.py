import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatModel, MessageModel
from django.contrib.auth.models import User
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"]
        # Send message to room group
        try:
          await save_ChatModel(self.room_name,message,user)
          print(self.room_name)
        except:
          print('An exception occurred')
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": f"{user}:{message}"}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        
@database_sync_to_async
def save_ChatModel(room_name, message, user):
    user = User.objects.get(username = user)
    room,created = ChatModel.objects.get_or_create(room_name = room_name)
    room.user.add(user)
    return MessageModel.objects.create(room_name = room,message = message, user= user)