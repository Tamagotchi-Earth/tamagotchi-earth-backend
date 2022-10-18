from typing import Optional
from rest_framework import serializers
from .models import Product, UserProductInfo


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
            'default_portion_size_override'
        )
        read_only_fields = (
            'id',
            'name',
            'icon',
            'is_green',
            'type',
            'hint',
            'default_portion_size'
        )

    # This solution is hacky but it works
    default_portion_size_override = serializers.SerializerMethodField()

    def get_default_portion_size_override(self, obj) -> Optional[float]:
        # Read portion size set by user or None
        request = self.context['request']
        try:
            value = obj.user_info.get(user_id=request.user.id).default_portion_size_override
            return value
        except UserProductInfo.DoesNotExist:
            return None

    # def update(self, instance, validated_data):
    #     if '_default_portion_size_override' in validated_data:
    #         default_portion_size_override = validated_data.get('_default_portion_size_override')
    #         request = self.context['request']
    #         user_info_obj, created = instance.user_info.get_or_create(user_id=request.user.id, defaults={
    #             'default_portion_size_override': default_portion_size_override
    #         })
    #         if not created:
    #             user_info_obj.default_portion_size_override = default_portion_size_override
    #             user_info_obj.save()
    #     return super(ProductSerializer, self).update(instance, validated_data)


class UserProductInfoSerializer(serializers.ModelSerializer):
    """Serializer for UserProductInfo model"""

    class Meta:
        model = UserProductInfo
        fields = (
            'default_portion_size_override',
        )
