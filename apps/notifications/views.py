from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=NotificationSerializer
    def get_queryset(self): return Notification.objects.filter(user=self.request.user)
    @action(detail=True,methods=['post'])
    def read(self,request,pk=None):
        obj=self.get_object(); obj.is_read=True; obj.save(update_fields=['is_read']); return Response(self.get_serializer(obj).data)
    @action(detail=False,methods=['post'])
    def read_all(self,request):
        self.get_queryset().update(is_read=True); return Response({'message':'All notifications marked as read.'})
