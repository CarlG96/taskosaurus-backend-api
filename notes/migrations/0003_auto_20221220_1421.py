# Generated by Django 3.2.16 on 2022-12-20 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0002_note_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='owner',
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE,
                to='auth.user'),
            preserve_default=False,
        ),
    ]
