# Generated by Django 4.1.3 on 2022-12-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0052_delete_cart_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sunglasses',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
