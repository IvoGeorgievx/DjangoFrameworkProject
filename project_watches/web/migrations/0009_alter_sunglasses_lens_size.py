# Generated by Django 4.1.3 on 2022-12-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_sunglasses_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sunglasses',
            name='lens_size',
            field=models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], max_length=20),
        ),
    ]
