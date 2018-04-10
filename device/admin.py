from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

import pkg_resources

from brewpi_webservice.admin import admin_site
from .models import Device


@admin.register(Device, site=admin_site)
class DeviceParentAdmin(PolymorphicParentModelAdmin):
    """
    Polymorphic parent model for devices in the admin
    """
    base_model = Device

    def get_child_models(self):
        """
        Provide child Actuators listing through entry points
        cf. https://django-polymorphic.readthedocs.org/en/latest/admin.html#the-parent-model
        """
        child_models = []
        for ep in pkg_resources.iter_entry_points(group='controller.device.admin'):
            admin_model = ep.load()
            child_models.append((admin_model.base_model, admin_model))

        return child_models


class DeviceAdmin(PolymorphicChildModelAdmin):
    pass


class DeviceInline(admin.StackedInline):
    extra = 0

    def has_add_permission(self, request):
        return True


class ActuatorInline(DeviceInline):
    readonly_fields = ['actuator_ptr']


class SensorInline(DeviceInline):
    readonly_fields = ['sensor_ptr']
