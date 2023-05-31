from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from django.urls import include, path, re_path, reverse_lazy
from .root import RootView

router = DefaultRouter()

urlpatterns = [
    path("", RootView.as_view()),
    path("api/v1/", include(router.urls)),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
