"""
File for the url routing for the
'tasks.urls' section of the
Taskosaurus API. Displays both a list view
and a detail view of specific Tasks.
"""
from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>', views.TaskDetailView.as_view()),
]
