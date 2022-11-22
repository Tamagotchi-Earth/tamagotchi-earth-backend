from typing import Optional
from rest_framework import serializers
from .models import Product, UserProductInfo, UserProductConsumption


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
            'default_portion_size',
            'ghg',
            'land',
            'water',
            'footprint_per_unit',
            'default_portion_size_override'
        )
        read_only_fields = (
            'id',
            'name',
            'icon',
            'is_green',
            'type',
            'hint',
            'ghg',
            'land',
            'water',
            'footprint_per_unit',
            'default_portion_size'
        )

    footprint_per_unit = serializers.FloatField(read_only=True)
    default_portion_size_override = serializers.SerializerMethodField()

    def get_default_portion_size_override(self, obj) -> Optional[float]:
        # Read portion size set by user or None
        request = self.context['request']
        try:
            value = obj.user_info.get(user_id=request.user.id).default_portion_size_override
            return value
        except UserProductInfo.DoesNotExist:
            return None


class UserProductInfoSerializer(serializers.ModelSerializer):
    """Serializer for UserProductInfo model"""

    class Meta:
        model = UserProductInfo
        fields = (
            'default_portion_size_override',
        )


class UserProductConsumptionSerializer(serializers.ModelSerializer):
    """Serializer for UserProductConsumption model"""

    class Meta:
        model = UserProductConsumption
        fields = (
            'id',
            'product',
            'product_id',
            'portion_size',
            'date',
            'user',
            'footprint'
        )
        read_only_fields = (
            'id',
            'product',
            'footprint'
        )

    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(source='product', queryset=Product.objects.all(), write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    footprint = serializers.FloatField(read_only=True)
