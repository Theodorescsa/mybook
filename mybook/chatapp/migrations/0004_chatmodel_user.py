# Generated by Django 4.2.6 on 2024-05-17 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0003_remove_chatmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmodel',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]