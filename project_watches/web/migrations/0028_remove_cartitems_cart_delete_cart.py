# Generated by Django 4.1.3 on 2022-12-06 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_alter_belts_image_alter_sunglasses_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
