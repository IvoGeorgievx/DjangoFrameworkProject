# Generated by Django 4.1.3 on 2022-12-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_wallet_wallets'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunglasses',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
