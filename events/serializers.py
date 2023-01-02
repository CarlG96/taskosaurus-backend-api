"""
Serializer file for the Event class.
"""
from django.utils import timezone
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Class to serialize Event information returned from
    database. Adds extras fields displaying the id of the
    Event, who owns the specific Event and whether the
    user is the owner of the Event.
    """
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Function to return whether or not the user is
        the owner.

        Parameters:
        obj: Event object being checked to see whether the user is
        the owner.

        Return:
        bool
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_is_overdue(self, obj):
        """
        Function to return whether or not the event is overdue.

        Parameter:
        obj: Event object being checked.
        Return:
        bool
        """
        now = timezone.now()
        if obj.date_of_event < now:
            return True
        else:
            return False

    class Meta:
        """
        Class which displays which fields are to be included in the
        serializer.
        """
        model = Event
        fields = [
            'title', 'date_created', 'date_updated', 'date_of_event',
            'need_travel', 'money_required', 'owner', 'is_owner',
            'id', 'is_overdue'
        ]