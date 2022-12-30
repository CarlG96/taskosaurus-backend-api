from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Event(models.Model):
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
  
                                                     

    
