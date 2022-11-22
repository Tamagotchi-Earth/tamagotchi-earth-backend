from django.db.models.aggregates import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from apps.products.models import Product, UserProductConsumption
from .serializers import PersonalStatsResponseSerializer


class PersonalStatsView(APIView):
    """Information about current user's ecological footprint and other data"""

    @extend_schema(responses=PersonalStatsResponseSerializer)
    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        qs = UserProductConsumption.objects.filter(user_id=user_id)
        consumed_count = qs.count()
        if not consumed_count:
            return Response(PersonalStatsResponseSerializer({
                'products_consumed': 0,
                'unique_products_consumed': 0,
                'most_popular_product': None,
                'total_footprint': 0,
                'average_footprint': 0,
                'total_ghg': 0,
                'average_ghg': 0,
                'total_land': 0,
                'average_land': 0,
                'total_water': 0,
                'average_water': 0,
            }, context={'request': self.request}).data)
        product_id = qs.values('product').annotate(count=Count('product')).order_by('-count').first()['product']
        most_popular = Product.objects.get(id=product_id)
        footprint_list, ghg_list, land_list, water_list = zip(*([
            (
                obj.product.footprint_per_unit * obj.portion_size,
                obj.product.ghg * obj.portion_size,
                obj.product.land * obj.portion_size,
                obj.product.water * obj.portion_size
            )
            for obj in qs
        ]))
        return Response(PersonalStatsResponseSerializer({
            'products_consumed': consumed_count,
            'unique_products_consumed': len(set(qs.values_list('product_id', flat=True))),
            'most_popular_product': most_popular,
            'total_footprint': sum(footprint_list),
            'average_footprint': sum(footprint_list) / consumed_count,
            'total_ghg': sum(ghg_list),
            'average_ghg': sum(ghg_list) / consumed_count,
            'total_land': sum(land_list),
            'average_land': sum(land_list) / consumed_count,
            'total_water': sum(water_list),
            'average_water': sum(water_list) / consumed_count,
        }, context={'request': self.request}).data)
