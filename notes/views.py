from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from taskosaurus_api.permissions import IsOwnerOrReadOnly


class NoteList(APIView):
    def get(self, request):
        current_task = self.request.task
        notes = Note.objects.filter(task==current_user, )
        serializer = NoteSerializer(notes, many=True, context={'request': request})
        return Response(serializer.data)


class NoteDetailView(APIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            note = Note.objects.get(pk=pk)
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
