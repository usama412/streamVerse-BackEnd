from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
@shared_task
def send_verification_email(email,username,token):
 url=f"{settings.FRONTEND_URL}/verify-email?token={token}"
 send_mail('Verify your StreamVerse account',f'Hi {username}, verify your account: {url}',settings.DEFAULT_FROM_EMAIL,[email])
@shared_task
def send_password_reset_email(email,token):
 url=f"{settings.FRONTEND_URL}/reset-password?token={token}"
 send_mail('Reset your StreamVerse password',f'Reset your password here: {url}',settings.DEFAULT_FROM_EMAIL,[email])
