from django.test import TestCase
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from .factories import TaskFactory
from ..serializers import CreateTaskSerializer


class TestCreateUserSerializer(TestCase):
    def setUp(self):
        self.task_data = model_to_dict(TaskFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateTaskSerializer(data={})
        assert serializer.is_valid() == False

    def test_serializer_with_valid_data(self):
        serializer = CreateTaskSerializer(data=self.task_data)
        assert serializer.is_valid() == True
