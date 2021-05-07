from django.conf import settings
from django.db import models


class Products(models.Model):
    "Generated Model"
    shoes = models.CharField(
        max_length=256,
    )
    sneakers = models.ForeignKey(
        "storeapp.Product",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="products_sneakers",
    )


class Product(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    price = models.FloatField()
    image = models.URLField()


# Create your models here.
