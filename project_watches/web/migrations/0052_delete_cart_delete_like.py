# Generated by Django 4.1.3 on 2022-12-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0051_remove_watches_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
