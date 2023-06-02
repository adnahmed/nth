from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id"]


class CreateTaskSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    class Meta:
        model = Task
        fields = ["id"]  # TODO: Change this to Task required fields
