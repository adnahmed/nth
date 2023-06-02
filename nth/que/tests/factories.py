import factory


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "que.Task"
        # django_get_or_create = ("id",)

    id = factory.Faker("uuid4")
