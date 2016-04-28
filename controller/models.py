from django.db import models
from django.utils.translation import ugettext as _


class Controller(models.Model):
    """
    A Hardware Controller that holds sensors and actuators
    """
    name = models.CharField(max_length=255, unique=True)
    uri = models.CharField(max_length=255, unique=True,
                           help_text=_("Which address to connect to, e.g. http://10.42.42.10"))
    description = models.TextField(blank=True, null=True)
    alive = models.BooleanField(default=False,
                                help_text=_("Whether this device has been online during the last few seconds."))

    def __str__(self):
        return self.name
