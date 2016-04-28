from django.db import models
from django.utils.translation import ugettext as _

from device.models import Sensor

class TemperatureSensor(Sensor):
    value = models.FloatField(null=True)


class HumiditySensor(Sensor):
    """
    Senses humidity in the air
    """
    value = models.FloatField(null=True)
