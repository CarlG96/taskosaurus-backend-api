"""
File for url routing for the whole Taskosaurus backend API.
Includes paths for admin, Tasks, Events, Profiles, authorisation
and root routes.
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('', include('profiles.urls')),
    path('', include('tasks.urls')),
    path('', include('events.urls')),
    path('', include('notes.urls')),
]
