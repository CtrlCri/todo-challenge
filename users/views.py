from rest_framework import generics

from users.serializers import UserSerializer
from .models import User

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
