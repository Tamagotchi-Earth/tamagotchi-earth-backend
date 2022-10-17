from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    """Food and drinks (list, retrieve)"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
