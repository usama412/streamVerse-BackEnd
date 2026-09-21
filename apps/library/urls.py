from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MyListViewSet,HistoryViewSet,ReviewViewSet
router=DefaultRouter(); router.register('user/my-list',MyListViewSet,basename='my-list'); router.register('user/history',HistoryViewSet,basename='history')
urlpatterns=router.urls+[path('content/<int:content_id>/reviews/',ReviewViewSet.as_view({'get':'list','post':'create'})),path('content/<int:content_id>/reviews/<int:pk>/',ReviewViewSet.as_view({'get':'retrieve','patch':'partial_update','delete':'destroy'}))]
