# Generated by Django 3.2.16 on 2023-02-19 14:28

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_date_of_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_of_event',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 2, 20, 14, 28, 41, 304427, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2025, 11, 15, 14, 28, 41, 304436, tzinfo=utc))]),
        ),
    ]
