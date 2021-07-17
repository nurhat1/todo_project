from rest_framework import serializers

from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'deadline', 'is_executed']


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        validated_data["is_executed"] = False
        return Task.objects.create(**validated_data)
