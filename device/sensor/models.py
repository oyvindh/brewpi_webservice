from django.utils.translation import ugettext as _

from ..models import Sensor

class TemperatureSensor(Sensor):
    @property
    def get_value(self):
        return 0


class HumiditySensor(Sensor):
    """
    Senses humidity in the air
    """
    @property
    def get_value(self):
        return 0
