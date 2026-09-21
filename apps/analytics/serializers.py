from rest_framework import serializers
from .models import PlaybackEvent
class PlaybackEventSerializer(serializers.ModelSerializer):
    class Meta: model=PlaybackEvent; fields='__all__'; read_only_fields=['user']
