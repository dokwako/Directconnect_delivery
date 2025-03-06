from django.contrib import admin

# Register your models here.
from .models import Merchant, DeliveryPatern, order

admin.site.register(Merchant)
admin.site.register(DeliveryPatern)
admin.site.register(order)