# Generated by Django 4.1.3 on 2022-12-03 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0025_alter_profile_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='preffered_ties',
            new_name='preferred_ties',
        ),
    ]