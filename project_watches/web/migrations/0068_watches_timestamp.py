# Generated by Django 4.1.3 on 2022-12-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0067_remove_watches_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='watches',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
