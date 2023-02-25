from product.serializers import ProductSerializer
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Order
        fields = (
            "name",
            "address",
            "city",
            "phone",
            "item_name",
            "item_size",
            "item_price",
        )