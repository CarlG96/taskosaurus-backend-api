"""
File for rendering Profile views in the
Taskosaurus API.
"""
from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from taskosaurus_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Class that displays a list of all the Profile
    Models created and currently stored in the
    database.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    Class that displays a specific Profile Model. Allows get and put
    requests if the user is the owner of the Profile allowing them
    to update their profile should they wish to.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
