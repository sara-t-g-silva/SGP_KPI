# Generated by Django 5.0.6 on 2024-06-17 14:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rpa', '0006_error_rpa_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpa_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='rpa_model',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
