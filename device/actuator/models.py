from django.db import models
from django.utils.translation import ugettext as _

from ..models import PWMActuator

class DS2413Actuator(PWMActuator):
    """
    1-wire, 2 canals PWM Actuator
    """
    class Meta:
        verbose_name = 'DS2413'
        verbose_name_plural = 'DS2413'

    OUTPUT_CHOICES = (
        ('A', 'A'),
        ('B', 'B')
    )
    PIN_TYPE_CHOICES = (
        ('I', _("Inverted")),
        ('NI', _("Not Inverted"))
    )

    output = models.CharField(choices=OUTPUT_CHOICES, max_length=1)
    pin_type = models.CharField(choices=PIN_TYPE_CHOICES, max_length=20)

    @property
    def get_status(self):
        return 0
