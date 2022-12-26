"""
File for the url routing for the
'notes.urls' section of the
Taskosaurus API. Displays both a list view
and a detail view of specific Notes.
"""
from django.urls import path
from notes import views

urlpatterns = [
    path('notes/', views.NoteList.as_view()),
    path('notes/<int:pk>', views.NoteDetailView.as_view())
]
