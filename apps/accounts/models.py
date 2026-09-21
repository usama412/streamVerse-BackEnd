import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    email=models.EmailField(unique=True)
    avatar=models.URLField(blank=True)
    bio=models.TextField(blank=True)
    email_verified=models.BooleanField(default=False)
    is_premium=models.BooleanField(default=False)
    verification_token=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    reset_token=models.UUIDField(null=True, blank=True, unique=True)
    reset_token_expires=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'; REQUIRED_FIELDS=['username']
    def __str__(self): return self.email
