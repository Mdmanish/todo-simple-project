from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo


class RegisterUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

class LoginUserSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()


class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = '__all__'
		extra_kwargs = {
			'user': {'read_only': True},
			'created_at': {'read_only': True},
			'modified_at': {'read_only': True}
		}
