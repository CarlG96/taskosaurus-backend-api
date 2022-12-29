"""
File for rendering Task views in the
Taskosaurus API.
"""
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from taskosaurus_api.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """
    Class that displays a list of all the Task
    Models created and currently stored in the
    database. Also allows authenticated users
    to post new Task Models.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['state', 'priority']
    search_fields = ['title', 'state', 'priority']
    
    def get_queryset(self):
        """
        Makes it so only the Tasks that the user owns are available.

        Parameters: None

        Return: queryset
        """
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Function which saves a new Task Model to the
        database.

        Parameters:
        serializer: The serializer used, in this
        case the TaskSerializer would be used.

        Returns:
        void, just saves the Task.
        """
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class that displays a specific Task Model. Allows get, put
    and delete requests to be made if the user is authenticated.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()

    def get_queryset(self):
        """
        Makes it so only the Tasks that the user owns are available.

        Parameters: None

        Return: queryset
        """
        return self.queryset.filter(owner=self.request.user)
