"""
File for rendering views in the
Taskosaurus API.
"""
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwnerOrReadOnly


class NoteList(generics.ListCreateAPIView):
    """
    Class that displays a list of all the Note
    Models created and currently stored in the
    database. Also allows authenticated users
    to post new Note Models.
    """
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Note.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['task', 'task__owner__profile']
    search_fields = ['task__owner__username', 'title']

    def perform_create(self, serializer):
        """
        Function which saves a new Note Model to the
        database.

        Parameters:
        serializer: The serializer used, in this
        case the NoteSerializer would be used.

        Returns:
        void, just saves the Note.
        """
        serializer.save()


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class that displays a specific Note Model. Allows get, put
    and delete requests to be made if the user is authenticated.
    """
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.all()
