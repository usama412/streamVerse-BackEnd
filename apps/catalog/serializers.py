from rest_framework import serializers
from .models import *
class GenreSerializer(serializers.ModelSerializer):
    class Meta: model=Genre; fields='__all__'
class PersonSerializer(serializers.ModelSerializer):
    class Meta: model=Person; fields='__all__'
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta: model=Episode; fields=['id','season','number','title','description','thumbnail','video_url','duration','air_date','views']
class SeasonSerializer(serializers.ModelSerializer):
    episodes=EpisodeSerializer(many=True,read_only=True)
    class Meta: model=Season; fields=['id','number','title','episodes']
class ContentSerializer(serializers.ModelSerializer):
    genres=GenreSerializer(many=True,read_only=True); cast=PersonSerializer(many=True,read_only=True); seasons=SeasonSerializer(many=True,read_only=True)
    class Meta: model=Content; fields=['id','title','slug','content_type','description','poster','backdrop','trailer','video_url','year','duration','rating','genres','language','country','quality','cast','director','tags','seasons','views','is_featured']
class LiveSerializer(serializers.ModelSerializer):
    class Meta: model=LiveEvent; fields=['id','category','viewers','start_time','is_live']
