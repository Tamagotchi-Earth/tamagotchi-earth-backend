from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model (read-only)"""

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'icon',
            'is_green',
            'type',
            'hint',
            'default_portion_size'
        )
        read_only_fields = fields
