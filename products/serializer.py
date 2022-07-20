from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'regular_price': {'write_only': True}
        }
        model = Product
        fields = (
            'id',
            'name',
            'price_in_sale',
            'regular_price',
            'description',
        )