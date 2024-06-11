from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	description = models.TextField(null=True, blank=True)
	deadline = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
