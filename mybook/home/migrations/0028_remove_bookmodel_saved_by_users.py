# Generated by Django 4.2.6 on 2023-11-23 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_bookmodel_saved_by_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='saved_by_users',
        ),
    ]
