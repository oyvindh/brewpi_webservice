from django.core.management.base import BaseCommand

from controller.models import Controller
from datasync.brewpi_04x import BrewPi04xSyncher


class Command(BaseCommand):
    help = 'Discover Devices of Controllers and update their status'

    def handle(self, *args, **options):
        for controller in Controller.objects.all():
            p = BrewPi04xSyncher(controller)
            p.read_sensor_states()
            p.update_controller_model(save=True)

            if not controller.alive:
                self.stdout.write(
                    self.style.ERROR(
                        'Controller "{0}" ({1}) seems unreachable, marked offline'
                        .format(controller.name, controller.uri)
                    )
                )
            else:
                self.stdout.write(self.style.SUCCESS('Successfully updated controller "%s"' % controller.name))
