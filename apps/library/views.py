from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

class MyListViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=MyListSerializer
    http_method_names=['get','post','delete']
    def get_queryset(self): return MyList.objects.filter(user=self.request.user).select_related('content')
    def create(self,request,*args,**kwargs):
        obj,_=MyList.objects.get_or_create(user=request.user,content_id=request.data.get('content'))
        return Response(self.get_serializer(obj).data,status=201)

class HistoryViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=HistorySerializer
    http_method_names=['get','post','patch','delete']
    def get_queryset(self): return WatchHistory.objects.filter(user=self.request.user).select_related('content','episode')
    def create(self,request,*args,**kwargs):
        obj,_=WatchHistory.objects.update_or_create(user=request.user,content_id=request.data.get('content'),episode_id=request.data.get('episode'),defaults={'progress_seconds':request.data.get('progress_seconds',0),'duration_seconds':request.data.get('duration_seconds',0)})
        return Response(self.get_serializer(obj).data,status=201)
    @action(detail=False,methods=['delete'])
    def clear(self,request): self.get_queryset().delete(); return Response(status=204)

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    serializer_class=ReviewSerializer
    http_method_names=['get','post','patch','delete']
    def get_queryset(self): return Review.objects.filter(content_id=self.kwargs.get('content_id')).select_related('user')
    def perform_create(self,serializer): serializer.save(user=self.request.user,content_id=self.kwargs['content_id'])
    def perform_update(self,serializer): serializer.save(user=self.request.user)
