import time
import json
import requests

from django.core.management.base import BaseCommand, CommandError

from controller.models import Controller
from device.models import Sensor, Actuator
from device.sensor.models import TemperatureSensor
from device.actuator.models import DS2413Actuator


class Command(BaseCommand):
    help = 'Discover Devices of Controllers and update their status'

    def handle(self, *args, **options):
        for controller in Controller.objects.all():
            try:
                #requests.post("{0}/{1}".format(controller.uri, "socketmessage.php"), data={'messageType': 'refreshDeviceList'})
                #time.sleep(2)
                response = requests.post("{0}/{1}".format(controller.uri, "socketmessage.php"), data={'messageType': 'getDeviceList'})
                controller.alive = True
            except requests.exceptions.ConnectionError:
                self.stdout.write(self.style.ERROR('Controller "{0}" ({1}) seems unreachable, marked offline'.format(controller.name, controller.uri)))
                controller.alive = False
                controller.save()

            if controller.alive:
                try:
                    data = json.loads(response.content.decode("utf-8"))
                except ValueError:
                    self.stdout.write(self.style.ERROR('Controller "{0}" ({1}) seems unreachable, marked offline'.format(controller.name, controller.uri)))

                controller.description = "Board {0} with shield {1}".format(data["board"], data["shield"])

                for device in data['deviceList']['installed']:
                    uri = "onewire://{0}".format(device['a'])
                    # Sensors
                    try:
                        sensor = Sensor.objects.get(uri=uri, controller=controller)
                    except Sensor.DoesNotExist:
                        if device['h'] == 2: # Temp Sensor
                            sensor = TemperatureSensor.objects.create(uri=uri, controller=controller)
                            self.stdout.write(self.style.SUCCESS('Created installed Temperature Sensor ({0})'.format(sensor.uri)))

                    # Actuators
                    try:
                        actuator = Actuator.objects.get(uri=uri, controller=controller)
                    except Actuator.DoesNotExist:
                        if device['h'] == 3: # DS2413
                            actuator = DS2413Actuator.objects.create(uri=uri, controller=controller)
                            self.stdout.write(self.style.SUCCESS('Created installed DS2413 Actuator ({0})'.format(actuator.uri)))

                controller.save()

                self.stdout.write(self.style.SUCCESS('Successfully updated controller "%s"' % controller.name))
