# Generated by Django 4.1.3 on 2022-12-07 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0033_remove_profile_image_url_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cart_items',
        ),
    ]
