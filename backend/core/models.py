from django.db import models
from django.contrib.auth.models import User

# Merchant model represents businesses using our platform.
class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.business_name


# DeliveryPatern - people handling deliveries
class DeliveryPatern(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Fixed 'User' to 'user'
    vehicle_type = models.CharField(
        max_length=255,
        choices=[
            ('bicycle', 'Bicycle'),
            ('motorcycle', 'Motorcycle'),
            ('truck', 'Truck'),
            ('van', 'Van'),
        ]
    )
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_type}"


# Order - represents a delivery order
class Order(models.Model):  # Renamed from 'order' to 'Order' (avoids conflict with Python keywords)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    delivery_patern = models.ForeignKey(DeliveryPatern, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15)  # Field for customer's phone number
    delivery_address = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.customer_name} - {self.status}"
