"""
Code for registering Profile models to the
admin site for CRUD functionality for
the admin.
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
