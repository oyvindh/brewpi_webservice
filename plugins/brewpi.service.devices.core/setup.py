import os
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = "brewpi.service.devices.core",
    description='Core device support for the BrewPi Service',
    version = "0.1",
    packages = find_packages(),
    namespace_packages = ['devices.core'],
    entry_points = {
        'controller.device.model': [
            'ds2413 = devices.core.actuator.models:DS2413Actuator'
        ],
        'controller.device.admin': [
            'ds2413 = devices.core.actuator.admin:DS2413ActuatorAdmin',
            'temp_sensor = devices.core.sensor.admin:TemperatureSensorAdmin',
            'humidity_sensor = devices.core.sensor.admin:HumiditySensorAdmin',
        ],
        'controller.device.inline_admin': [
            'ds2413 = devices.core.actuator.admin:DS2413ActuatorInline',
            'temp_sensor = devices.core.sensor.admin:TemperatureSensorInline',
            'humidity_sensor = devices.core.sensor.admin:HumiditySensorInline',
        ]
    }
)
