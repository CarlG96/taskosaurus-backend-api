from django.db import models
from django.contrib.auth.models import User


class Task (models.Model):
    CURRENT = 'CU'
    ARCHIVED = 'AC'
    STATE_CHOICES = [
        (CURRENT, 'current'),
        (ARCHIVED, 'archived')
    ]
    MUST_DO = 'MUD'
    MIGHT_DO = 'MID'
    CAN_DO = 'CAD'
    PRIORITY_CHOICES = [
        (MUST_DO, 'must do'),
        (MIGHT_DO, 'might do'),
        (CAN_DO, 'can do')
    ]
    due_date = models.DateField(blank=False)
    date_created = models.DateField(auto_now_add=True)
    state = models.CharField(
        max_length=2, choices=STATE_CHOICES, default=CURRENT
    )
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True, max_length=500)
    priority = models.CharField(
        max_length=3, choices=PRIORITY_CHOICES, default=MUST_DO
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['state', '-date_created']

    def __str__(self):
        return f'{title}'