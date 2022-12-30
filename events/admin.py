"""
Code for registering Event models to the
admin site for CRUD functionality for
the admin.
"""
from django.contrib import admin
from .models import Event

admin.site.register(Event)
