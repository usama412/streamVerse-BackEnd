from django.conf import settings
from django.db import models
from apps.catalog.models import Content
class PlaybackEvent(models.Model): user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL); content=models.ForeignKey(Content,on_delete=models.CASCADE); event=models.CharField(max_length=40); position_seconds=models.PositiveIntegerField(default=0); session_id=models.CharField(max_length=100,blank=True); created_at=models.DateTimeField(auto_now_add=True)
