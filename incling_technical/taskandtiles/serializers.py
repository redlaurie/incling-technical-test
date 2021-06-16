from rest_framework import serializers
from .models import Task,Tile

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = '__all__'