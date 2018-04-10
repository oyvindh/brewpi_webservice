import json
import time
from urllib.parse import urljoin

from multimethod import multimethod
import requests

from device.sensor.models import TemperatureSensor
from device.actuator.models import DS2413Actuator

from .abstract import AbstractSyncher


class BrewPi04xSyncher(AbstractSyncher):
    """
    Model Data Syncher for existing BrewPi Web UI (BrewPi v0.4.x)
    """

    (SENSOR_TEMPERATURE,
     ACTUATOR_DS2413) = range(2, 4)

    device_model_mapping = {SENSOR_TEMPERATURE: TemperatureSensor,
                            ACTUATOR_DS2413: DS2413Actuator}

    def __init__(self, aController):
        self.controller = aController
        self.script_path = "socketmessage.php"
        self.full_uri = urljoin(aController.uri, self.script_path)
        self.device_data = None

    def _refresh_device_list(self, read_values: bool) -> bool:
        """
        Ask the controller to internally refresh its device list
        """
        requests.post(self.full_uri, data={'messageType': 'refreshDeviceList', 'message': 'readValues'})

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
            time.sleep(3)
            self.device_data = self._get_device_list()
        except requests.exceptions.ConnectionError:
            return False

        return True

    def _update_device_models(self, save=False):
        """
        Update values of device models for this controller
        """
        for device_data in self.device_data['deviceList']['installed']:
            device_class = self.device_model_mapping[device_data['h']]

            device = self._update_installed_device_model(device_class,
                                                         self.controller,
                                                         slot_id=device_data['i'],
                                                         data=device_data)

            if device and save:
                device.save()

    def update_controller_model(self, save=False) -> bool:
        """
        Update the controller model
        """
        if self.device_data is not None:
            self.controller.alive = False
        else:
            self.controller.alive = True
            self._update_device_models(save=True)

        if save:
            self.controller.save()

        return self.controller.alive

    @multimethod(TemperatureSensor)
    def _update_model(aModel, data) -> bool:
        """
        Update a Temperature Sensor
        """
        aModel.value = data['v']

        return True

    @multimethod(DS2413Actuator)
    def _update_model(aModel, data) -> bool:
        """
        Update a DS2413 Actuator
        """
        # Pin inversion
        if data['x'] == 0:
            aModel.inverted = False
        else:
            aModel.inverted = True

        aModel.pio = data['n']

        return True
