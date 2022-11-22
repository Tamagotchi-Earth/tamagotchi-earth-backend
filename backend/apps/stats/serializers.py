from rest_framework import serializers

from apps.products.serializers import ProductSerializer


class PersonalStatsResponseSerializer(serializers.Serializer):  # noqa
    products_consumed = serializers.IntegerField()
    unique_products_consumed = serializers.IntegerField()
    most_popular_product = ProductSerializer(allow_null=True)
    total_footprint = serializers.FloatField()
    average_footprint = serializers.FloatField()
    total_ghg = serializers.FloatField()
    average_ghg = serializers.FloatField()
    total_land = serializers.FloatField()
    average_land = serializers.FloatField()
    total_water = serializers.FloatField()
    average_water = serializers.FloatField()
