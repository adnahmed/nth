from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory
from ..models import Task
from .factories import TaskFactory

fake = Faker()


class TestTaskListTestCase(APITestCase):
    """
    Tests /task list operations.
    """

    def setUp(self):
        self.url = reverse("task-list")
        self.task_data = factory.build(dict, FACTORY_CLASS=TaskFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.task_data)
        assert response.status_code == status.HTTP_201_CREATED

        task = Task.objects.get(pk=response.data.get("id"))
        assert task.id == self.task_data.get("id")


class TestTaskDetailTestCase(APITestCase):
    """
    Tests /task detail operations.
    """

    def setUp(self):
        self.task = TaskFactory()
        self.url = reverse("task-detail", kwargs={"pk": self.task.pk})

    def test_get_request_returns_a_given_task(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
