# Generated by Django 4.2.6 on 2023-11-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='saved',
            field=models.BooleanField(default=False),
        ),
    ]
