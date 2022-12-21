from django.http import Http404
from rest_framework import status, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwnerOrReadOnly


class NoteList(APIView):
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    filter_backends = [filters.SearchFilter]
    filter_fields = ['owner', 'title', 'task']
    search_fields = ['owner', 'title', 'task']

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            note = Note.objects.get(pk=pk)
            task = note.task
            self.check_object_permissions(self.request, note)
            return note
        except Note.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        note = self.get_object(pk)
        note.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
