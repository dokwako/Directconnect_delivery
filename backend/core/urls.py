# a router generates urls automaticaly for the viewsets

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MerchantViewSet, DeliveryPaternViewSet, OrderViewSet


# Create a router and register our viewset with it.

router = DefaultRouter()
router.register(r'merchants', MerchantViewSet)  # merchants api
router.register(r'deliverypaterns', DeliveryPaternViewSet) # deliverypaterns api
router.register(r'orders', OrderViewSet) # orders api

urlpatterns = [
    path('api/', include(router.urls)),
]