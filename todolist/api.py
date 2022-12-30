from .models import Todolist
from rest_framework import ( 
    viewsets, 
    authentication, 
    permissions,
    filters
)
from .serializers import TodolistSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    #queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    
    def get_queryset(self):
        request_user = self.request.user  # El usuario que ha iniciado sesión
        return Todolist.objects.filter(user=request_user)
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends =[filters.SearchFilter]
    search_fields = ['description', 'created_at']