# Generated by Django 4.1.3 on 2022-11-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_menswatches_image'),
        ('auth_app', '0002_profile_preferred_watches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='preferred_watches',
        ),
        migrations.AddField(
            model_name='profile',
            name='preferred_watches',
            field=models.ManyToManyField(blank=True, null=True, to='web.menswatches'),
        ),
    ]