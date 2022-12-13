# Generated by Django 4.1.3 on 2022-12-06 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_delete_cart'),
        ('auth_app', '0031_remove_profile_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.cartitems'),
        ),
    ]
