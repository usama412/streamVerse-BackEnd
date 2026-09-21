from rest_framework import viewsets,permissions
from .models import PlaybackEvent
from .serializers import PlaybackEventSerializer

class PlaybackEventViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    serializer_class=PlaybackEventSerializer
    http_method_names=['post','get']
    def get_queryset(self): return PlaybackEvent.objects.filter(user=self.request.user)
    def perform_create(self,serializer): serializer.save(user=self.request.user)
