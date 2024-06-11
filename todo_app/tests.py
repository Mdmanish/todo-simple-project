from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Todo


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'username': 'test_user',
            'password': '1234',
            'email': 'test_user@gmail.com'
        }

    def test_register_user(self):
        response = self.client.post('/register/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginViewTest(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(username="test_user", password="1234")

	def test_login_user(self):
		response = self.client.post('/login/', {'username':'test_user', 'password':'1234'})
		self.assertTrue('access_token' in response.data)
		self.assertTrue('refresh_token' in response.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoListCreateViewTest(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(username='test_user', password='1234')
		self.client.force_authenticate(user=self.user)
		self.valid_payload = {
			'name': 'Test Task',
            'description': 'Test Description',
            'deadline': '2024-12-31T23:59:59'
		}

	def test_create_todo_task(self):
		response = self.client.post('/api/todos/', self.valid_payload)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_todo_list(self):
		Todo.objects.create(name='Test Task', description='Test Description', user=self.user)
		response = self.client.get('/api/todos/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)


class TodoRetrieveUpdateDeleteViewTest(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(username='test_user', password='1234')
		self.client.force_authenticate(user=self.user)
		self.todo_obj = Todo.objects.create(name='Test Task', description='Test Description', deadline='2024-12-31T23:59:59', user=self.user)

	def test_retriev_todo_task(self):
		response = self.client.get(f'/api/todos/{self.todo_obj.id}/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_todo_task(self):
		payload = {'name': 'Updated task name'}
		response = self.client.put(f'/api/todos/{self.todo_obj.id}/', payload)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'Updated task name')

	def test_delete_todo_task(self):
		response = self.client.delete(f'/api/todos/{self.todo_obj.id}/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Todo.objects.filter(user=self.user).count(), 0)
