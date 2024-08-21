# tasks_app/serializers.py

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Verifica se os campos obrigatórios estão presentes.
        """
        if 'title' not in data:
            raise serializers.ValidationError({"title": "This field is required."})
        if 'description' not in data:
            raise serializers.ValidationError({"description": "This field is required."})
        if 'due_date' not in data:
            raise serializers.ValidationError({"due_date": "This field is required."})
        return data