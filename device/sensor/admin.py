from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from brewpi_webservice.admin import admin_site
from .models import Sensor, TemperatureSensor, HumiditySensor

class SensorChildAdmin(PolymorphicChildModelAdmin):
    base_model = Sensor

class TemperatureSensorAdmin(SensorChildAdmin):
    base_model = TemperatureSensor

class HumiditySensorAdmin(SensorChildAdmin):
    base_model = HumiditySensor


@admin.register(Sensor, site=admin_site)
class SensorParentAdmin(PolymorphicParentModelAdmin):
    list_display = ('label', 'uri', 'controller')
    base_model = Sensor
    child_models = (
        (TemperatureSensor, TemperatureSensorAdmin),
        (HumiditySensor, HumiditySensorAdmin),
    )

class TemperatureSensorInline(admin.StackedInline):
    model = TemperatureSensor
    #fk_name = 'temperaturesensor'
    readonly_fields = ['sensor_ptr']
    extra = 0

class HumiditySensorInline(admin.StackedInline):
    model = HumiditySensor
    #fk_name = 'temperaturesensor'
    readonly_fields = ['sensor_ptr']
    extra = 0
