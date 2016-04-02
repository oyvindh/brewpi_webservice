import pkg_resources

from behave import given, when, then

from django.core.management import call_command

from controller.models import Controller
from controller.admin import ControllerAdmin
from device.models import Device

@given("There's a controller device model plugin available")
def step_impl(context):
    context.controller = Controller.objects.create(name="Test Controller")
    assert len(list(pkg_resources.iter_entry_points(group='controller.device.model'))) > 0

@when(u'I activate its model')
def step_impl(context):
    for ep in pkg_resources.iter_entry_points(group='controller.device.model'):
        context.new_device_model = ep.load()

@then(u'the model can be used')
def step_impl(context):
    new_device = context.new_device_model.objects.create(controller=context.controller)
    assert new_device in Device.objects.all()



@given(u'There\'s a controller device admin plugin available')
def step_impl(context):
    context.controller = Controller.objects.create(name="Test Controller")
    assert len(list(pkg_resources.iter_entry_points(group='controller.device.inline_admin'))) > 0

@when(u'I activate its admin model')
def step_impl(context):
    for ep in pkg_resources.iter_entry_points(group='controller.device.inline_admin'):
        context.admin_inline_model = ep.load()

@then(u'the inline is loaded in the controller administration model')
def step_impl(context):
    assert context.admin_inline_model in ControllerAdmin.inlines
