from django.db import models
from django.utils.translation import ugettext as _

from polymorphic.models import PolymorphicModel

from controller.models import Controller

class Device(PolymorphicModel):
    """
    Any hardware device (sensor, actuator) that is connected to a Controller
    """
    class Meta:
        abstract = True
        # unique_together = (('controller', 'assigned_id'),)

    label = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, help_text=_("A device URI such as onewire://182377282"))
    assigned_id = models.PositiveIntegerField(blank=True, null=True, help_text=_("The ID assigned by the Controller"))

    @property
    def is_assigned(self):
        return self.assigned_id != None

    def __str__(self):
        return self.label or "Unnamed device (uri={0})".format(self.uri)

class Sensor(Device):
    """
    A sensor is an object whose purpose is to detect events or changes
    in its environment, and then provide a corresponding output.
    """
    controller = models.ForeignKey(Controller, related_name='sensors')

class Actuator(Device):
    """
    An actuator is a type of motor that is responsible for moving or
    controlling a mechanism or system.
    """
    controller = models.ForeignKey(Controller, related_name='actuators')

class PWMActuator(Actuator):
    """
    An actuator that is driven by Pulse Width Modulation (PWM)
    """
    class Meta:
        abstract = True
