"""
Serializer file for the Note class.
"""
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Class to serialize Note information returned from
    database. Adds extras fields displaying the id of the
    Note, who owns the specific Note and whether the
    user is the owner of the Note.
    """

    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='task.owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Function to return whether or not the user is
        the owner

        Parameters:
        obj: Note object being checked to see whether the user is
        the owner.

        Return:
        bool
        """
        request = self.context['request']
        return request.user == obj.task.owner

    class Meta:
        """
        Class which displays which fields are to be included in the
        serializer.
        """
        model = Note
        fields = [
            'title', 'description', 'date_created', 'date_updated', 'task',
            'owner', 'is_owner', 'id'
        ]
