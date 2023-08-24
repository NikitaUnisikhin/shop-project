from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.apps.catalog.urls')),
    path('api/', include('core.apps.cart.urls')),
    path('api/', include('core.apps.accounts.urls')),
    path('api/', include('core.apps.orders.urls')),
]
