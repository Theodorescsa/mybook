# Generated by Django 4.2.6 on 2023-10-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_bookmodel_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='link_image',
            field=models.TextField(default=False),
        ),
    ]
