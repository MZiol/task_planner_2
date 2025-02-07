from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'assigned_user']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Nazwa jest wymagana.")
        return value