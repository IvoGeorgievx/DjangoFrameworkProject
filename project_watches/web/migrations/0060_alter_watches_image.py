# Generated by Django 4.1.3 on 2022-12-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0059_alter_belts_options_alter_sunglasses_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watches',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]