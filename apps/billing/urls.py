from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter(); router.register('subscriptions/plans',PlanViewSet,basename='plans'); router.register('subscriptions',SubscriptionViewSet,basename='subscriptions')
urlpatterns=router.urls
