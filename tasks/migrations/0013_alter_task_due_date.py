# Generated by Django 3.2.16 on 2022-12-30 11:07

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 12, 31, 11, 7, 58, 872405, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2025, 9, 25, 11, 7, 58, 872421, tzinfo=utc))]),
        ),
    ]
