# Generated by Django 4.1.3 on 2022-12-02 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0015_alter_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='preferred_women_watches',
        ),
    ]
