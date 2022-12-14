# Generated by Django 3.2.16 on 2022-12-20 18:33

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(
                validators=[django.core.validators.MinValueValidator(
                    datetime.datetime(2022, 12, 21, 18, 33, 34, 6445,
                                      tzinfo=utc)),
                            django.core.validators.MaxValueValidator(
                    datetime.datetime(2025, 9, 15, 18, 33, 34, 6467,
                                      tzinfo=utc))]),
        ),
    ]
