from behave import given, when, then

from controller.models import Controller

@given(u'we have a controller')
def step_impl(context):
    c = Controller.objects.create()

@when(u'I represent it as a string')
def step_impl(context):
    c = Controller.objects.get(id=1)

@then(u'it shows a nice string')
def step_impl(context):
    c = Controller.objects.get(id=1)
    print(c)
