# Generated by Django 4.1.3 on 2022-12-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_remove_cartitems_cart_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='web.cartitems')),
            ],
        ),
    ]