"""
Code for registering Task models to the
admin site for CRUD functionality for
the admin.
"""
from django.contrib import admin
from .models import Task

admin.site.register(Task)
