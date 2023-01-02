"""
Serializer file for the Task class.
"""
from django.utils import timezone
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Class to serialize Task information returned from
    database. Adds extras fields displaying the id of the
    Task, who owns the specific Task and whether the
    user is the owner of the Task.
    """
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()

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
        return request.user == obj.owner

    def get_is_overdue(self, obj):
        """
        Function to return whether or not the task is overdue.

        Parameter:
        obj: Task object being checked.
        Return:
        bool
        """
        now = timezone.now()
        if obj.due_date < now:
            return True
        else:
            return False

    class Meta:
        """
        Class which displays which fields are to be included in the
        serializer.
        """
        model = Task
        fields = [
            'due_date', 'date_created', 'state', 'title', 'description',
            'priority', 'owner', 'is_owner', 'date_updated', 'id', 'is_overdue'
        ]
