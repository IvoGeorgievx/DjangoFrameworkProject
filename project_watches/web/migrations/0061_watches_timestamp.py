# Generated by Django 4.1.3 on 2022-12-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0060_alter_watches_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='watches',
            name='timestamp',
            field=models.DateTimeField(default='2022-12-18T00:00:00.000000'),
            preserve_default=False,
        ),
    ]
