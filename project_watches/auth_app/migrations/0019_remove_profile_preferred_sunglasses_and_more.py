# Generated by Django 4.1.3 on 2022-12-02 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_sunglasses_price'),
        ('auth_app', '0018_profile_preferred_sunglasses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='preferred_sunglasses',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='preferred_wallets',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='preferred_watches',
        ),
        migrations.AddField(
            model_name='profile',
            name='preferred_sunglasses',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.sunglasses'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='preferred_wallets',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.wallets'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='preferred_watches',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.watches'),
            preserve_default=False,
        ),
    ]
