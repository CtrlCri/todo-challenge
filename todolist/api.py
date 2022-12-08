from .models import Todolist
from rest_framework import ( 
    viewsets, 
    authentication, 
    permissions,
    filters
)
from .serializers import TodolistSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends =[filters.SearchFilter]
    search_fields = ['description', 'created_at']