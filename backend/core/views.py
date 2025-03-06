from django.shortcuts import render

# Create your views here. - handles get,post,put,delete requests automatically
from rest_framework import viewsets
from rest_framework import permissions
from .models import Merchant, DeliveryPatern, order
from .serializers import MerchantSerializer, DeliveryPaternSerializer, OrderSerializer



class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()    # Fetches all merchants from the database.
    serializer_class = MerchantSerializer  # Converts the merchant data to JSON format.
    permission_classes = [permissions.IsAuthenticated]  # Ensures that only authenticated users can access the API.

class DeliveryPaternViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPatern.objects.all()
    serializer_class = DeliveryPaternSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
