from .models import Todolist
from rest_framework import viewsets, permissions
from .serializers import TodolistSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodolistSerializer