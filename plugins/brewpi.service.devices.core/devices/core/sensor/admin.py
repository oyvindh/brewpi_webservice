from django.contrib import admin

from device.admin import DeviceAdmin, SensorInline

from brewpi_webservice.admin import admin_site
from .models import Sensor, TemperatureSensor, HumiditySensor

@admin.register(TemperatureSensor, site=admin_site)
class TemperatureSensorAdmin(DeviceAdmin):
    base_model = TemperatureSensor

@admin.register(HumiditySensor, site=admin_site)
class HumiditySensorAdmin(DeviceAdmin):
    base_model = HumiditySensor


class TemperatureSensorInline(SensorInline):
    model = TemperatureSensor


class HumiditySensorInline(SensorInline):
    model = HumiditySensor
