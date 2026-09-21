from rest_framework import viewsets; from .models import BlogPost; from .serializers import BlogSerializer
class BlogViewSet(viewsets.ReadOnlyModelViewSet): queryset=BlogPost.objects.filter(published=True).select_related('author'); serializer_class=BlogSerializer; lookup_field='slug'; search_fields=['title','excerpt','content','category','tags']
