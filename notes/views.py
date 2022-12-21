from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwnerOrReadOnly


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Note.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['task', 'task__owner__profile']
    search_fields = ['task__owner__username', 'title']
    
    def perform_create(self, serializer):
        serializer.save()


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.all()