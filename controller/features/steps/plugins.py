import pkg_resources

from behave import given, when, then

from django.core.management import call_command

from controller.models import Controller
from device.models import Device

@given("I have a controller device plugin")
def step_impl(context):
    context.controller = Controller.objects.create(name="Test Controller")
    assert len(list(pkg_resources.iter_entry_points(group='controller'))) > 0

@when(u'I activate it')
def step_impl(context):
    for ep in pkg_resources.iter_entry_points(group='controller.device.model'):
        context.new_device_model = ep.load()
        call_command('migrate')

@then(u'the device becomes available')
def step_impl(context):
    new_device = context.new_device_model.objects.create(controller=context.controller)
    print(Device.objects.all())
    assert new_device in Device.objects.all()


