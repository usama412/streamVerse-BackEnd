from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
class GenreViewSet(viewsets.ReadOnlyModelViewSet): queryset=Genre.objects.all(); serializer_class=GenreSerializer; lookup_field='slug'
class PersonViewSet(viewsets.ReadOnlyModelViewSet): queryset=Person.objects.all(); serializer_class=PersonSerializer
class ContentViewSet(viewsets.ReadOnlyModelViewSet):
 queryset=Content.objects.filter(is_published=True).prefetch_related('genres','cast','seasons__episodes'); serializer_class=ContentSerializer; filterset_fields=['content_type','year','language','quality','is_featured']; search_fields=['title','description','tags','genres__name','cast__name']; ordering_fields=['created_at','rating','views','year']; lookup_field='pk'
 @action(detail=False,methods=['get'])
 def trending(self,request): return Response(self.get_serializer(self.get_queryset().order_by('-views')[:20],many=True).data)
 @action(detail=False,methods=['get'])
 def search(self,request):
  q=request.query_params.get('q',''); qs=self.get_queryset().filter(title__icontains=q) if q else self.get_queryset(); return Response(self.get_serializer(qs[:50],many=True).data)
 @action(detail=True,methods=['get'])
 def episodes(self,request,pk=None): return Response(EpisodeSerializer(Episode.objects.filter(season__content_id=pk),many=True).data)
class LiveEventViewSet(viewsets.ReadOnlyModelViewSet): queryset=LiveEvent.objects.select_related('content').filter(content__is_published=True); serializer_class=LiveSerializer
