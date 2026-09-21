from rest_framework import serializers
from .models import *
from apps.catalog.serializers import ContentSerializer
class MyListSerializer(serializers.ModelSerializer):
    content=ContentSerializer(read_only=True)
    class Meta: model=MyList; fields=['id','content','created_at']
class HistorySerializer(serializers.ModelSerializer):
    content=ContentSerializer(read_only=True)
    class Meta: model=WatchHistory; fields=['id','content','episode','progress_seconds','duration_seconds','watched_at']
class ReviewSerializer(serializers.ModelSerializer):
    user_name=serializers.CharField(source='user.username',read_only=True)
    class Meta: model=Review; fields=['id','user_name','rating','body','created_at','updated_at']; read_only_fields=['id','user_name']
