from rest_framework import serializers
from .models import BlogPost
class BlogSerializer(serializers.ModelSerializer):
    author_name=serializers.CharField(source='author.username',read_only=True); date=serializers.DateTimeField(source='published_at',read_only=True)
    class Meta: model=BlogPost; fields=['id','slug','title','excerpt','content','image','category','author_name','date','read_time','tags']
