from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView
from apps.accounts.views import LoginView, RegisterView, LogoutView, MeView, VerifyEmailView, ForgotPasswordView, ResetPasswordView
urlpatterns=[
 path('admin/',admin.site.urls), path('api/auth/register/',RegisterView.as_view()), path('api/auth/login/',LoginView.as_view()), path('api/auth/refresh/',TokenRefreshView.as_view()), path('api/auth/logout/',LogoutView.as_view()), path('api/auth/me/',MeView.as_view()), path('api/auth/verify-email/',VerifyEmailView.as_view()), path('api/auth/forgot-password/',ForgotPasswordView.as_view()), path('api/auth/reset-password/',ResetPasswordView.as_view()),
 path('api/',include('apps.catalog.urls')), path('api/',include('apps.library.urls')), path('api/',include('apps.billing.urls')), path('api/',include('apps.blog.urls')), path('api/',include('apps.notifications.urls')), path('api/',include('apps.analytics.urls')),
 path('api/schema/',SpectacularAPIView.as_view(),name='schema'), path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui')]
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
