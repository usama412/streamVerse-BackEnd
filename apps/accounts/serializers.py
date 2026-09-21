from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name','avatar','bio','email_verified','is_premium','created_at']
        read_only_fields=['id','email_verified','is_premium','created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    class Meta:
        model=User
        fields=['username','email','password','first_name','last_name']
    def validate_password(self,v):
        validate_password(v); return v
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    def validate(self,attrs):
        user=authenticate(email=attrs['email'],password=attrs['password'])
        if not user: raise serializers.ValidationError('Invalid email or password.')
        if not user.is_active: raise serializers.ValidationError('Account is disabled.')
        attrs['user']=user; return attrs
