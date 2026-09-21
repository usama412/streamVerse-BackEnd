from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
@admin.register(User)
class CustomUserAdmin(UserAdmin):
 fieldsets=UserAdmin.fieldsets+(('StreamVerse',{'fields':('avatar','bio','email_verified','is_premium','verification_token','reset_token','reset_token_expires')}),)
