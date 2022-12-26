"""
Code for the Note class which acts as a model for
the API backend of Taskosaurus.
"""
from django.db import models
from tasks.models import Task
from django.contrib.auth.models import User


class Note(models.Model):
    """
    Class for the Note Model.
    Attributes:
    id (int): Auto-generated attribute which represents unique id.
    title (str): Represents the title of the Note.
    date_created (DateTime): Date and time of creation of the Note.
    date_updated (DateTime): Date and time Note was last updated.
    task (ForeignKey): Primary key of Task that this Note is linked
    with.
    """
    title = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=False, max_length=1500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}'
