from rest_framework.routers import DefaultRouter
from .views import PlaybackEventViewSet
router=DefaultRouter(); router.register('analytics/playback',PlaybackEventViewSet,basename='playback'); urlpatterns=router.urls
