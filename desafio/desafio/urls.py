from django.urls import path
from api.views import UserCreateView

urlpatterns = [
    # outras URLs podem estar aqui
    
    path('api/create-user/', UserCreateView.as_view(), name='user-create'),
]
