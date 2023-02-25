from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Order(models.Model):
    name = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=100, null=True)
    item_name = models.CharField(max_length=255,null=True)
    item_size = models.IntegerField(default=0,null=True)
    item_price = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name