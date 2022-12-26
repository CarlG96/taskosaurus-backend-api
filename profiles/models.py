"""
Code for the Profile class which acts as a model for
the API backend of Taskosaurus.
"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Class for the Profile Model.
    Attributes:
    id (int): Auto-generated attribute which represents unique id (hidden).
    owner (OneToOne): Represents a one-to-one relationship with
    a specific User instance.
    date_created (DateTime): Date and time of creation of the Profile.
    date_updated (DateTime): Date and time Profile was last updated.
    image (file): Image that is displayed in the user's profile.
    Represents the user.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40, blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_dktbdx'
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function which creates the Profile.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
