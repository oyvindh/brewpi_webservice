"""
This module holds all the generic Models about devices
"""

from django.db import models
from django.utils.translation import ugettext as _

from polymorphic.models import PolymorphicModel

from controller.models import Controller

class Device(PolymorphicModel):
    """
    Any hardware device (sensor, actuator) that is connected to a Controller
    """
    label = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, help_text=_("A device URI such as onewire://182377282"))
    slot = models.PositiveIntegerField(blank=True, null=True, help_text=_("The slot ID assigned paired with the Controller"))
    controller = models.ForeignKey(Controller, related_name='devices')

    @property
    def is_installed(self):
        return self.slot != None

    def __str__(self):
        return self.label or "Unnamed device (uri={0})".format(self.uri)

class Sensor(Device):
    """
    A sensor is an object whose purpose is to detect events or changes
    in its environment, and then provide a corresponding output.
    """
    pass

class Actuator(Device):
    """
    An actuator is a type of motor that is responsible for moving or
    controlling a mechanism or system.
    """
    pass

class PWMActuator(Actuator):
    """
    An actuator that is driven by Pulse Width Modulation (PWM)
    """
    class Meta:
        abstract = True
