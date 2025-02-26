from django.core.management.base import BaseCommand
from webapp.models import Client, Order

class Command(BaseCommand):
    help = 'Clears all client and order data'

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        Client.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all data')) 