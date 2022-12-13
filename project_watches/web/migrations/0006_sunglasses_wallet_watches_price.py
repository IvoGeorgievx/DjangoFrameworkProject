# Generated by Django 4.1.3 on 2022-12-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_menswatches_watches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sunglasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('image', models.URLField()),
                ('model_year', models.PositiveIntegerField()),
                ('lens_size', models.PositiveIntegerField()),
                ('lens_color', models.CharField(max_length=15)),
                ('frame_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('size', models.CharField(max_length=20)),
                ('image', models.URLField()),
                ('ID_window', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('coin_pouch', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('card_capacity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='watches',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]