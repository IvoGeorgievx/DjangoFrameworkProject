# Generated by Django 4.1.3 on 2022-12-07 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0034_remove_profile_cart_items'),
        ('web', '0040_remove_like_to_watches_like_to_watches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.profile'),
        ),
    ]