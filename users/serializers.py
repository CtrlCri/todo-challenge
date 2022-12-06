from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password']
        read_only_fields = ('password',)
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password =validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user