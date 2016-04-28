from django.contrib import admin

from brewpi_webservice.admin import admin_site

from device.models import Actuator
from device.admin import DeviceAdmin, ActuatorInline

from .models import DS2413Actuator


@admin.register(DS2413Actuator, site=admin_site)
class DS2413ActuatorAdmin(DeviceAdmin):
    base_model = DS2413Actuator

class DS2413ActuatorInline(ActuatorInline):
    model = DS2413Actuator
