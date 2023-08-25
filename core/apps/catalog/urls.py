from django.urls import path
from . import views

urlpatterns = [
    path('catalog/products/', views.products),
    path('catalog/products/<int:id>/', views.product_by_id)
]

