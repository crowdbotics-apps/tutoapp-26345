from django.conf import settings
from django.db import models


class Products(models.Model):
    "Generated Model"
    shoes = models.CharField(
        max_length=256,
    )


# Create your models here.
