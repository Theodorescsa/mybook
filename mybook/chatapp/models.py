from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatModel(models.Model):
    user = models.ManyToManyField(User)
    room_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room_name
class MessageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.ForeignKey(ChatModel,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message