import uuid
from datetime import timedelta
from django.contrib.auth import login
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .tasks import send_verification_email, send_password_reset_email
class RegisterView(APIView):
 permission_classes=[AllowAny]
 def post(self,request):
  s=RegisterSerializer(data=request.data); s.is_valid(raise_exception=True); user=s.save(); send_verification_email.delay(user.email,user.username,str(user.verification_token)); return Response({'message':'Registration successful. Check your email to verify your account.','user':UserSerializer(user).data},status=201)
class LoginView(APIView):
 permission_classes=[AllowAny]
 def post(self,request):
  from .serializers import LoginSerializer
  s=LoginSerializer(data=request.data); s.is_valid(raise_exception=True); u=s.validated_data['user']; r=RefreshToken.for_user(u); return Response({'access':str(r.access_token),'refresh':str(r),'user':UserSerializer(u).data})
class LogoutView(APIView):
 permission_classes=[IsAuthenticated]
 def post(self,request):
  token=request.data.get('refresh')
  if token:
   try: RefreshToken(token).blacklist()
   except Exception: pass
  return Response({'message':'Logged out successfully.'})
class MeView(APIView):
 permission_classes=[IsAuthenticated]
 def get(self,request): return Response(UserSerializer(request.user).data)
 def patch(self,request):
  s=UserSerializer(request.user,data=request.data,partial=True); s.is_valid(raise_exception=True); s.save(); return Response(s.data)
class VerifyEmailView(APIView):
 permission_classes=[AllowAny]
 def post(self,request):
  token=request.data.get('token'); u=User.objects.filter(verification_token=token).first()
  if not u: return Response({'detail':'Invalid token.'},status=400)
  u.email_verified=True; u.save(update_fields=['email_verified']); return Response({'message':'Email verified successfully.'})
class ForgotPasswordView(APIView):
 permission_classes=[AllowAny]
 def post(self,request):
  email=request.data.get('email'); u=User.objects.filter(email=email).first()
  if u:
   u.reset_token=uuid.uuid4(); u.reset_token_expires=timezone.now()+timedelta(hours=1); u.save(update_fields=['reset_token','reset_token_expires']); send_password_reset_email.delay(u.email,str(u.reset_token))
  return Response({'message':'If the account exists, a reset email has been sent.'})
class ResetPasswordView(APIView):
 permission_classes=[AllowAny]
 def post(self,request):
  u=User.objects.filter(reset_token=request.data.get('token'),reset_token_expires__gt=timezone.now()).first()
  if not u: return Response({'detail':'Invalid or expired token.'},status=400)
  from django.contrib.auth.password_validation import validate_password
  password=request.data.get('password'); validate_password(password,u); u.set_password(password); u.reset_token=None; u.reset_token_expires=None; u.save(); return Response({'message':'Password reset successfully.'})
