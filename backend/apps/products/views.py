from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema
from .models import Product, UserProductInfo, UserProductConsumption
from .serializers import ProductSerializer, UserProductInfoSerializer, UserProductConsumptionSerializer
from common.pagination import CustomPageNumberPagination


class ProductViewSet(ReadOnlyModelViewSet):
    """Food and drinks (list, retrieve)"""
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Product.objects.all()

    @extend_schema(request=UserProductInfoSerializer)
    @action(detail=True, methods=['patch'], url_path='set_user_info')
    def set_user_info(self, request, *args, **kwargs):
        """Set fields exclusive to current user"""
        product = self.get_object()
        serializer = UserProductInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserProductInfo.objects.update_or_create(product_id=product.id, user_id=request.user.id,
                                                 defaults=serializer.validated_data)
        return Response(self.get_serializer(product).data)


class UserProductConsumptionViewSet(ModelViewSet):
    """List of products consumed by current user"""
    serializer_class = UserProductConsumptionSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return UserProductConsumption.objects.filter(user_id=self.request.user.id).order_by('-date')
