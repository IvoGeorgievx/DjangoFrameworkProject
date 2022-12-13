# Generated by Django 4.1.3 on 2022-12-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0038_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='to_watches',
        ),
        migrations.AddField(
            model_name='like',
            name='to_watches',
            field=models.ManyToManyField(blank=True, null=True, to='web.watches'),
        ),
    ]
