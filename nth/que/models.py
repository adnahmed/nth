import uuid
from django.db import models


class Task(models.Model):
    # TODO: Add more fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.id
