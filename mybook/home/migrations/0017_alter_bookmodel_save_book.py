# Generated by Django 4.2.6 on 2023-11-08 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_bookmodel_save_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='save_book',
            field=models.BooleanField(null=True),
        ),
    ]
