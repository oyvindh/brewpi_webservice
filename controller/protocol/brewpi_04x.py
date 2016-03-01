import json
import time
from urllib.parse import urljoin

import requests

from device.sensor.models import TemperatureSensor
from device.actuator.models import DS2413Actuator

class BrewPi04x(object):
    """
    Connection Layer for existing BrewPi Web UI (BrewPi v0.4.x)
    """

    (SENSOR_TEMPERATURE,
     ACTUATOR_DS2413) = range(2, 4)

    def __init__(self, aController):
        self.controller = aController
        self.script_path = "socketmessage.php"
        self.full_uri = urljoin(aController.uri, self.script_path)
        self.device_data = None

    def _refresh_device_list(self, read_values : bool) -> bool:
        """
        Ask the controller to internally refresh its device list
        """
        requests.post(self.full_uri, data={'messageType': 'refreshDeviceList', 'message': 'readValues'})
        time.sleep(3)

        return True

    def _get_device_list(self):
        """
        Retrieve the device list from the controller
        """
        response = requests.post(self.full_uri, data={'messageType': 'getDeviceList'})
        data = json.loads(response.content.decode("utf-8"))

        return data

    def read_sensor_states(self) -> bool:
        """
        Refresh and read state devices from the Controller
        """
        self.device_data = None

        try:
            self._refresh_device_list(read_values=True)
            self.device_data = self._get_device_list()
        except requests.exceptions.ConnectionError:
            return False

        return True

    def _update_temperature_sensor(self, uri, device_data):
        """
        Update a Temperature Sensor
        """
        device, created = TemperatureSensor.objects.get_or_create(uri=uri, controller=self.controller)

        # Temperature value
        device.value = device_data['v']

        return device

    def _update_ds2413_actuator(self, uri, device_data):
        """
        Update a DS2413 Actuator
        """
        device, created = DS2413Actuator.objects.get_or_create(uri=uri, pio=device_data['n'], controller=self.controller)

        # Pin inversion
        if device_data['x'] == 0:
            device.inverted = False
        else:
            device.inverted = True

        device.pio = device_data['n']

        return device


    def _update_device_models(self, save=False):
        """
        Update values of device models for this controller
        """
        for device_data in self.device_data['deviceList']['installed']:
            uri = "onewire://{0}".format(device_data['a'])

            if device_data['h'] == BrewPi04x.SENSOR_TEMPERATURE:
                device = self._update_temperature_sensor(uri, device_data)
            elif device_data['h'] == BrewPi04x.ACTUATOR_DS2413:
                device = self._update_ds2413_actuator(uri, device_data)

            device.slot = device_data['i']
            if save:
                device.save()

    def update_controller_model(self, save=False):
        """
        Update the controller model
        """
        if self.device_data == None:
            self.controller.alive = False
        else:
            self.controller.alive = True
            self._update_device_models(save=True)

        if save:
            self.controller.save()
