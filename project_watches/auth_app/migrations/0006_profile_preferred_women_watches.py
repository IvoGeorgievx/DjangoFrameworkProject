# Generated by Django 4.1.3 on 2022-11-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_womenwatches'),
        ('auth_app', '0005_rename_preferred_watches_profile_preferred_mens_watches'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preferred_women_watches',
            field=models.ManyToManyField(to='web.womenwatches'),
        ),
    ]
