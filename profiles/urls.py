"""
File for the url routing for the
'profiles.urls' section of the
Taskosaurus API. Displays both a list view
and a detail view of specific Profiles.
"""
from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>', views.ProfileDetailView.as_view()),
]
