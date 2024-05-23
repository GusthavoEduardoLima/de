from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('api/create_user/', UserCreate.as_view(), name='user-create'),
]
