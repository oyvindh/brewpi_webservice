from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from brewpi_webservice.admin import admin_site
from device.sensor.admin import TemperatureSensorInline, HumiditySensorInline
from device.actuator.admin import DS2413ActuatorInline

from .models import Controller

@admin.register(Controller, site=admin_site)
class ControllerAdmin(admin.ModelAdmin):
    list_display = ('name', 'uri', 'alive')
    inlines = [DS2413ActuatorInline, TemperatureSensorInline, HumiditySensorInline]
    readonly_fields = ['alive']
