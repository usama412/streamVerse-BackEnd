from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Plan.objects.filter(is_active=True)
    serializer_class=PlanSerializer

class SubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=SubscriptionSerializer
    def get_queryset(self): return Subscription.objects.filter(user=self.request.user).select_related('plan')
    @action(detail=False,methods=['post'])
    def checkout(self,request):
        plan=Plan.objects.get(pk=request.data['plan_id'],is_active=True)
        payment=Payment.objects.create(user=request.user,plan=plan,amount=plan.price,currency=plan.currency,provider=request.data.get('provider','manual'))
        return Response({'payment_id':payment.id,'status':payment.status,'message':'Payment created. Connect your payment provider webhook to activate the subscription.'},status=201)
