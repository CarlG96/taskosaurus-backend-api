"""
Code for registering Note models to the
admin site for CRUD functionality for
the admin.
"""

from django.contrib import admin
from .models import Note

admin.site.register(Note)
