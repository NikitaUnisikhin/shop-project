from django.urls import path
from . import views

urlpatterns = [
    path('api/orders/add/', views.add_order),
    path('api/orders/my/', views.my_orders),
    path('api/orders/clients/', views.clients_orders),
]
