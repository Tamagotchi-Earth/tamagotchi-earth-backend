from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, UserProductConsumptionViewSet

router = SimpleRouter()
router.register('list', ProductViewSet, basename='list')
router.register('consumption', UserProductConsumptionViewSet, basename='consumption')

urlpatterns = [
    path('', include(router.urls))
]
