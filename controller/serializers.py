from rest_framework import serializers

from .models import Controller


class DeviceSerializer(serializers.Serializer):
    pass


class ControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controller
        fields = ('name', 'url', 'alive')

    alive = serializers.BooleanField(read_only=True)
    # devices = DeviceSerializer(many=True, read_only=True)
