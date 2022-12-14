from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATE_CHOICES = [
        ('Current', 'Current'),
        ('Archived', 'Archived')
    ]
    PRIORITY_CHOICES = [
        ('Must do', 'Must do'),
        ('Might do', 'Might do'),
        ('Can do', 'Can do')
    ]
    due_date = models.DateField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    state = models.CharField(
        max_length=10, choices=STATE_CHOICES, default='Current'
    )
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True, max_length=500)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='Must do'
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['state', '-date_created']

    def __str__(self):
        return f'{self.title}'