from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Merchant, DeliveryPatern, Order
from .serializers import UserSerializer, MerchantSerializer, DeliveryPaternSerializer, OrderSerializer

# Register User API View
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Merchant API View
class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]  # Auth required

# DeliveryPatern API View
class DeliveryPaternViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPatern.objects.all()
    serializer_class = DeliveryPaternSerializer
    permission_classes = [IsAuthenticated]  # Requires login

# Order API View
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Auth required
