# Generated by Django 4.1.3 on 2022-12-03 13:46

from django.db import migrations, models
import project_watches.auth_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0026_rename_preffered_ties_profile_preferred_ties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[project_watches.auth_app.models.validate_name]),
        ),
    ]
