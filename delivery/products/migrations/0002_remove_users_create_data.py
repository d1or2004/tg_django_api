# Generated by Django 5.0.6 on 2024-06-11 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='create_data',
        ),
    ]