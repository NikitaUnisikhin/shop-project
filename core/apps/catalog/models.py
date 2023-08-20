from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
