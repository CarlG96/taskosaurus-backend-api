from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='task.owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.task.owner

    class Meta:
        model = Note
        fields = [
            'title', 'description', 'date_created', 'date_updated', 'task',
            'owner', 'is_owner'
        ]