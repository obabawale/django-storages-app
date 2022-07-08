from .models import Track
from rest_framework import viewsets, permissions
from .serializers import TrackSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all().order_by('id')
    serializer_class = TrackSerializer
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticated]
