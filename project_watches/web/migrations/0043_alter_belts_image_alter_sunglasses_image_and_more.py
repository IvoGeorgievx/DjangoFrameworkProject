# Generated by Django 4.1.3 on 2022-12-07 11:34

from django.db import migrations, models
import project_watches.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0042_alter_watches_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belts',
            name='image',
            field=models.ImageField(upload_to='static/images/', ),
        ),
        migrations.AlterField(
            model_name='sunglasses',
            name='image',
            field=models.ImageField(upload_to='static/images/', ),
        ),
        migrations.AlterField(
            model_name='ties',
            name='image',
            field=models.ImageField(upload_to='static/images/', ),
        ),
        migrations.AlterField(
            model_name='wallets',
            name='image',
            field=models.ImageField(upload_to='static/images/', ),
        ),
    ]
