from .models import Track
from rest_framework import serializers


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['albumart', 'mediafile',
                  'order', 'title', 'duration']
