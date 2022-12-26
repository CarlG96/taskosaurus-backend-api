from django.db import models
from tasks.models import Task
from django.contrib.auth.models import User


class Note(models.Model):
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
