from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from webapp.models import Client, Order
from faker import Faker
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Creates dummy data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create test user if it doesn't exist
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user('testuser', 'test@example.com', 'testpass123')
            self.stdout.write(self.style.SUCCESS('Created test user'))

        # Create clients
        for i in range(50):  # Create 50 dummy clients
            try:
                client = Client.objects.create(
                    full_name=fake.name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    address=fake.street_address(),
                    city=fake.city(),
                    state=fake.state(),
                    zipcode=fake.zipcode(),
                    total_orders=0,
                    total_spent=Decimal('0.00')
                )

                # Create orders for each client
                num_orders = random.randint(0, 5)
                for j in range(num_orders):
                    amount = Decimal(str(round(random.uniform(100, 1000), 2)))
                    Order.objects.create(
                        client=client,
                        order_number=f"{i}{j}{fake.unique.random_number(digits=6)}",
                        amount=amount,
                        status=random.choice(['pending', 'completed', 'cancelled']),
                        description=fake.text(max_nb_chars=200)
                    )
                self.stdout.write(f"Created client {i+1}/50 with {num_orders} orders")

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating client {i+1}: {str(e)}'))
                continue

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data')) 