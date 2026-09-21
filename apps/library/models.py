from django.conf import settings
from django.db import models
from apps.catalog.models import Content, Episode
class MyList(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='my_list'); content=models.ForeignKey(Content,on_delete=models.CASCADE); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=[('user','content')]
class WatchHistory(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='watch_history'); content=models.ForeignKey(Content,on_delete=models.CASCADE); episode=models.ForeignKey(Episode,null=True,blank=True,on_delete=models.CASCADE); progress_seconds=models.PositiveIntegerField(default=0); duration_seconds=models.PositiveIntegerField(default=0); watched_at=models.DateTimeField(auto_now=True)
    class Meta: unique_together=[('user','content','episode')]
class Review(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); content=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='reviews'); rating=models.PositiveSmallIntegerField(); body=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta: unique_together=[('user','content')]
class Profile(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profiles'); name=models.CharField(max_length=80); avatar=models.URLField(blank=True); is_kids=models.BooleanField(default=False)
    class Meta: unique_together=[('user','name')]
