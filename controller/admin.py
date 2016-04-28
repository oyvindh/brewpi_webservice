from django.contrib import admin

from brewpi_webservice.admin import admin_site

import pkg_resources

from .models import Controller

inline_admin_models = []
for ep in pkg_resources.iter_entry_points(group='controller.device.inline_admin'):
    inline_admin_models.append(ep.load())


@admin.register(Controller, site=admin_site)
class ControllerAdmin(admin.ModelAdmin):
    list_display = ('name', 'uri', 'alive')
    inlines = inline_admin_models
    readonly_fields = ['alive']
