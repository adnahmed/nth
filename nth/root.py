from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class RootView(GenericAPIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        return Response({"message": "NTH API for Crack.ME"})
