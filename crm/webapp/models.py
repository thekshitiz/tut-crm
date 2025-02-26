from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.
class Client(models.Model):
    """
    Client model for storing customer information
    """
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_orders = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        if not self.id:  # New instance
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email})"

class Order(models.Model):
    """
    Order model for tracking client purchases
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:  # New order
            self.client.total_orders += 1
            self.client.total_spent = Decimal(str(self.client.total_spent)) + self.amount
            self.client.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - {self.client.full_name}"
