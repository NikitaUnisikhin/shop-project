from django.db import models
from core.apps.basket.models import Buyer
from core.apps.catalog.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    delivery_address = models.TextField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
