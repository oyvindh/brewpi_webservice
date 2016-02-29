from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Controller
from .serializers import ControllerSerializer, DeviceSerializer

class DeviceViewSet(viewsets.ViewSet):
    def list(self, request, controller_pk=None):
        print("youpi")
        xx
        return Response()

    def retrieve(self, request, pk=None, controller_pk=None):
        print("youpi2")
        return Response(serializer.data)


class ControllerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage Controllers
    """
    queryset = Controller.objects.all().order_by('name')
    serializer_class = ControllerSerializer
