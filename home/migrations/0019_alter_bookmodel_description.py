# Generated by Django 4.2.6 on 2023-11-08 08:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_bookmodel_save_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
