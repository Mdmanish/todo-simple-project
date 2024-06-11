from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, LoginUserView, TodoListCreateView, TodoRetrieveUpdateDeleteView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh-view'),

    path('register/', RegisterUserView.as_view(), name='register-view'),
    path('login/', LoginUserView.as_view(), name='login-view'),

    path('api/todos/', TodoListCreateView.as_view(), name='todos-view'),
    path('api/todos/<int:todo_id>/', TodoRetrieveUpdateDeleteView.as_view(), name='todos-update-view'),

]
