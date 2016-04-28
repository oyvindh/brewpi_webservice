from rest_framework import viewsets
from rest_framework.response import Response

from .models import Controller
from .serializers import ControllerSerializer


class DeviceViewSet(viewsets.ViewSet):
    def list(self, request, controller_pk=None):
        print("list...")
        return Response()

    def retrieve(self, request, pk=None, controller_pk=None):
        print("retrieve...")
        return Response(serializer.data)


class ControllerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage Controllers
    """
    queryset = Controller.objects.all().order_by('name')
    serializer_class = ControllerSerializer
