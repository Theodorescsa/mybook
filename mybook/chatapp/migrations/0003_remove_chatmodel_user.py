# Generated by Django 4.2.6 on 2024-05-17 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_remove_chatmodel_message_messagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmodel',
            name='user',
        ),
    ]
