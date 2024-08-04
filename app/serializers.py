from rest_framework import serializers
from .models import *

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        exclude=['is_completed','created_at','updated_at']

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'
        depth=1
    
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'