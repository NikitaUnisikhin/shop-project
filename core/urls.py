from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.apps.catalog.urls')),
    path('api/', include('core.apps.cart.urls')),
    path('api/', include('core.apps.accounts.urls')),
    path('api/', include('core.apps.orders.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist')
]
