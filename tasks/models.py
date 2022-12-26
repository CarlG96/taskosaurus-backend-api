"""
Code for the Task class which acts as a model for
the API backend of Taskosaurus.
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(models.Model):
    """
    Class for the Task Model.
    Attributes:
    id (int): Auto-generated attribute which represents unique id (hidden).
    due_date (DateTime): Date and time when task must be completed by.
    Must be at least one day from the time of creation.
    date_created (DateTime): Date and time of creation of the Task.
    date_updated (DateTime): Date and time Task was last updated.
    state (enum): Represents whether the Task is current or has
    been completed and is therefore archived.
    title (str): Represents the title of the Task.
    description (str): Represents the description of the Task.
    priority (enum): Represents how urgent this task is specifically.
    Can be 'Must Do', 'Might Do' and 'Can Do'.
    owner (ForeignKey): Primary key of User that this Task is
    linked with.
    """
    STATE_CHOICES = [
        ('Current', 'Current'),
        ('Archived', 'Archived')
    ]
    PRIORITY_CHOICES = [
        ('Must do', 'Must do'),
        ('Might do', 'Might do'),
        ('Can do', 'Can do')
    ]
    due_date = models.DateTimeField(blank=False,
                                    validators=[MinValueValidator(
                                        timezone.now() + timezone.timedelta(
                                            days=1)),
                                                MaxValueValidator(
                                        timezone.now() + timezone.timedelta(
                                            days=1000))])
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='tasks')

    class Meta:
        ordering = ['state', '-date_created']

    def __str__(self):
        return f'{self.title}'
