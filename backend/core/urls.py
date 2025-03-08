# a router generates urls automaticaly for the viewsets

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MerchantViewSet, DeliveryPaternViewSet, OrderViewSet
from django.http import JsonResponse


# Create a router and register our viewset with it.

router = DefaultRouter()
router.register(r'merchants', MerchantViewSet)  # merchants api
router.register(r'deliverypaterns', DeliveryPaternViewSet) # deliverypaterns api
router.register(r'orders', OrderViewSet) # orders api


def home_view(request):
    return JsonResponse({'message':'Welcome to direct conect delivery API'})
urlpatterns = [
    path('',home_view, name = 'home'), # root url
    path('api/', include(router.urls)),
]