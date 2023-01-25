"""
File for the url routing for the
'events.urls' section of the
Taskosaurus API. Displays both a list view
and a detail view of specific Events.
"""
from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>', views.EventDetailView.as_view()),
]
