# Generated by Django 3.2.16 on 2023-02-19 14:28

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 2, 20, 14, 28, 41, 303533, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2025, 11, 15, 14, 28, 41, 303548, tzinfo=utc))]),
        ),
    ]
