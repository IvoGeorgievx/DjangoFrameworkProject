# Generated by Django 4.1.3 on 2022-12-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_sunglasses_lens_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sunglasses',
            name='lens_size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=20),
        ),
    ]
