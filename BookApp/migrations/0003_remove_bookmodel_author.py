# Generated by Django 4.2.16 on 2025-01-01 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0002_alter_bookmodel_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='author',
        ),
    ]
