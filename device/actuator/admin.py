from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from brewpi_webservice.admin import admin_site
from ..models import Actuator
from .models import DS2413Actuator

class ActuatorChildAdmin(PolymorphicChildModelAdmin):
    base_model = Actuator

class DS2413ActuatorAdmin(ActuatorChildAdmin):
    base_model = DS2413Actuator

@admin.register(Actuator, site=admin_site)
class ActuatorParentAdmin(PolymorphicParentModelAdmin):
    base_model = Actuator
    child_models = (
        (DS2413Actuator, DS2413ActuatorAdmin),
    )


class DS2413ActuatorInline(admin.StackedInline):
    model = DS2413Actuator
    #fk_name = 'temperaturesensor'
    readonly_fields = ['actuator_ptr']
    extra = 0

    def has_add_permission(self, request):
        return False
