"""
Code for the Event class which acts as a model for the
API backend of Taskosaurus.
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Event(models.Model):
    """
    Class for the Event Model.
    Attributes:
    id (int): Auto-generated attribute which represents unique id (hidden).
    date_created (DateTime): Date and time of creation of the Event.
    date_updated (DateTime): Date and time when Event was last updated.
    need_travel (bool): Represents whether the user must travel for this
    Event.
    money_required (int): Represents the amount of money required (est)
    for this Event. Defaults to 0 and cannot be negative.
    owner (ForeignKey): Primary key of User that this Event is
    linked with.
    """
    title = models.CharField(blank=False, max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_of_event = models.DateTimeField(blank=False,
                                         validators=[MinValueValidator(
                                                     timezone.now() +
                                                     timezone.timedelta(
                                                                        days=1)
                                                     ),
                                                     MaxValueValidator(
                                                     timezone.now() +
                                                     timezone.timedelta(
                                                                    days=1000)
                                                     )])
    need_travel = models.BooleanField(default=False)
    money_required = models.IntegerField(blank=False, default=0,
                                         validators=[MinValueValidator(0)]
                                         )
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='events')

    class Meta:
        ordering = ['-date_of_event']

    def __str__(self):
        return f'{self.title}'
