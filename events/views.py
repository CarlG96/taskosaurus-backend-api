"""
File for rendering Event views in the
Taskosaurus API.
"""
from django.http import Http404
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from taskosaurus_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    Class that displays a list of all the Event
    Models created and currently stored in the
    database owned by the user. Also allows authenticated users
    to post new Event Models.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['need_travel']
    search_fields = ['title', 'need_travel', 'money_required']
    
    def get_queryset(self):
        """
        Makes it so only the Events that the user owns are available.
        Q object makes it so an anonymous user cannot retrieve any
        information from the list view.

        Parameters: None

        Return: queryset
        """
        if self.request.user.is_anonymous:
            return self.queryset.filter(Q(pk=None))
        else:
            return self.queryset.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        """
        Function which saves a new Event Model to the
        database.

        Parameters:
        serializer: The serializer used, in this
        case the EventSerializer would be used.

        Returns:
        void, just saves the Event.
        """
        serializer.save(owner=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class that displays a specific Event Model. Allows get, put
    and delete requests to be made if the user is authenticated.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    def get_queryset(self):
        """
        Makes it so only the Events that the user owns are available.
        Q object makes it so an anonymous user cannot retrieve any
        information from the detail view.

        Parameters: None

        Return: queryset
        """
        if self.request.user.is_anonymous:
            return self.queryset.filter(Q(pk=None))
        else:
            return self.queryset.filter(owner=self.request.user)

