from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter(); router.register('movies',ContentViewSet,basename='content'); router.register('genres',GenreViewSet); router.register('people',PersonViewSet); router.register('live',LiveEventViewSet)
urlpatterns=router.urls
