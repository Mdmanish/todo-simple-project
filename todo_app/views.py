from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer, LoginUserSerializer, TodoSerializer
from django.contrib.auth import login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Todo

class RegisterUserView(APIView):

	def post(self, request):
		serializers = RegisterUserSerializer(data=request.data)
		if serializers.is_valid():
			user = serializers.save()
			user.set_password(serializers.validated_data['password'])
			user.save()
			login(request, user)
			return Response(serializers.data, status=status.HTTP_201_CREATED)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
	def post(self, request):
		serializers = LoginUserSerializer(data=request.data)
		if serializers.is_valid():
			username = serializers.validated_data['username']
			password = serializers.validated_data['password']
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				refresh = RefreshToken.for_user(user)
				return Response({'access_token': str(refresh.access_token), 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
			return Response({"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoListCreateView(APIView):
	def get(self, request):
		todo_obj = Todo.objects.filter(user=request.user)
		serializers = TodoSerializer(todo_obj, many=True)
		return Response(serializers.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializers = TodoSerializer(data=request.data)
		if serializers.is_valid():
			serializers.save(user=request.user)
			return Response(serializers.data, status=status.HTTP_201_CREATED)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoRetrieveUpdateDeleteView(APIView):
	def get(self, request, todo_id):
		todo_obj = get_object_or_404(Todo, pk=todo_id)
		serializer = TodoSerializer(todo_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, todo_id):
		todo_obj = get_object_or_404(Todo, pk=todo_id)
		serializer = TodoSerializer(todo_obj, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, todo_id):
		todo_obj = get_object_or_404(Todo, pk=todo_id)
		todo_obj.delete()
		return Response({"Todo task is deleted."}, status=status.HTTP_204_NO_CONTENT)
