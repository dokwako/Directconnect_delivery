from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import CreateUserView, MerchantViewSet, DeliveryPaternViewSet, OrderViewSet
from django.http import JsonResponse

# Router for ViewSets (Auto-generates URLs)
router = DefaultRouter()
router.register(r'merchants', MerchantViewSet)
router.register(r'deliverypaterns', DeliveryPaternViewSet)
router.register(r'orders', OrderViewSet)

def api_root(request):
    return JsonResponse({"message": "Welcome to the DirectConnect API. Use /api/ for endpoints."})

# URL Patterns
urlpatterns = [
    path("", api_root),  # Redirect root to API message
    path('admin/', admin.site.urls),

    # Authentication
    path('api/user/register/', CreateUserView.as_view(), name='register'),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API endpoints
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # DRF built-in login/logout

]
