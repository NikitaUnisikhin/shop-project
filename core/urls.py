from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('core.apps.catalog.urls')),
    path('cart/', include('core.apps.cart.urls')),
    path('accounts/', include('core.apps.accounts.urls')),
    path('orders/', include('core.apps.orders.urls')),
]
