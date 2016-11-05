from django.core.management.base import BaseCommand

from relay.population import create_village


class Command(BaseCommand):

    help = "Populates the database with some initial entries"

    def handle(self, *args, **options):
        create_village()
        self.stdout.write("Village population created!")
