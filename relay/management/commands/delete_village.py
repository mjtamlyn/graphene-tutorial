from django.core.management.base import BaseCommand

from relay.population import delete_village


class Command(BaseCommand):

    help = "Deletes all Streets, Houses, Persons from the database"

    def handle(self, *args, **options):
        delete_village()
        self.stdout.write("Village population deleted!")