# Generated by Django 4.1.3 on 2022-12-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_delete_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='belts',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='sunglasses',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='ties',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='wallets',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='watches',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='belts',
            field=models.ManyToManyField(blank=True, null=True, to='web.belts'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='sunglasses',
            field=models.ManyToManyField(blank=True, null=True, to='web.sunglasses'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='ties',
            field=models.ManyToManyField(blank=True, null=True, to='web.ties'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='wallets',
            field=models.ManyToManyField(blank=True, null=True, to='web.wallets'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='watches',
            field=models.ManyToManyField(blank=True, null=True, to='web.watches'),
        ),
    ]
