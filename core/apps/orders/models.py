from django.contrib.auth.models import User
from django.db import models
from core.apps.catalog.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    delivery_address = models.TextField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
