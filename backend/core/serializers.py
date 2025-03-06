from rest_framework import serializers
from .models import Merchant, DeliveryPatern, order

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'  #include all fields in the API

class DeliveryPaternSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPatern
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order   
        fields = '__all__'
        
