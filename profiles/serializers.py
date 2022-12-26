"""
Serializer file for the Profile class.
"""
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Class to serialize Profile information returned from the database.
    Adds two extra fields displaying the username of the person
    who owns the Profile and whether the current user is the owner
    of the Profile.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Function to identify whether the passed in
        image file is too large to be used for a
        Profile instance in order to ensure that
        Cloudinary can appropriately serve the
        images on the current plan being used by
        Taskosaurus. Raises a ValidationError if
        the file size, file height or file width
        are too large.

        Paramaters:
        value (file): File being checked.

        Returns:
        value (file) or ValidationError.
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

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

    class Meta:
        """
        Class which displays which fields are to be included in the
        serializer.
        """
        model = Profile
        fields = [
            'id', 'owner', 'date_created', 'date_updated', 'name', 'image',
            'is_owner'
        ]
