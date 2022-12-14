from django.db import models
from tasks.models import Task


class Note(models.Model):
    title = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=False, max_length=1500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}'
