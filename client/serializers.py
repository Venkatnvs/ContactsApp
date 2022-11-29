from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=0, write_only=True)
    email = serializers.EmailField(max_length=100, min_length=5)
    first_name = serializers.CharField(max_length=100, min_length=1)
    last_name = serializers.CharField(max_length=100, min_length=1)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already in use.')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, min_length=1)
    password = serializers.CharField(max_length=100, min_length=0, write_only=True)

    class Meta:
        model = User
        fields = ['username','password']