# Generated by Django 4.2.6 on 2023-11-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_bookmodel_save_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='customer',
        ),
    ]