import uuid
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from common.models import ModelBase
from common.utils import UUIDFilenameGenerator
from apps.users.models import CustomUser
from .enums import ProductTypes


class Product(ModelBase):
    """Food or drink with description and other metadata"""

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")
    name = models.CharField(max_length=255, verbose_name="product name")
    icon = models.ImageField(upload_to=UUIDFilenameGenerator(basepath='products'), blank=True, null=True,
                             verbose_name="icon")
    is_green = models.BooleanField(verbose_name="is green")
    type = models.CharField(max_length=8, choices=ProductTypes.choices, verbose_name="product type")
    hint = models.CharField(max_length=255, blank=True, verbose_name="hint")
    default_portion_size = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True,
                                             verbose_name="default user portion size")
    ghg = models.FloatField(validators=[MinValueValidator(0)], verbose_name="greenhouse gas amount")
    land = models.FloatField(validators=[MinValueValidator(0)], verbose_name="land area")
    water = models.FloatField(validators=[MinValueValidator(0)], verbose_name="water volume")

    @property
    def footprint_per_unit(self) -> float:
        """Ecological footprint for portion size 1"""
        # TODO: this is a mock formula
        return self.ghg + self.land + self.water

    def __str__(self):
        return str(self.name)


class UserProductInfo(ModelBase):
    """Custom information about product for user (override default portion size)"""

    class Meta:
        verbose_name = "user product info"
        verbose_name_plural = "user product info"
        constraints = [models.UniqueConstraint(fields=['product', 'user'], name='unique_product_user')]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user_info', verbose_name="product")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="user")
    default_portion_size_override = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True,
                                                      verbose_name="default user portion size")


class UserProductConsumption(ModelBase):
    """Information about specific time user consumed some food"""

    class Meta:
        verbose_name = "product consumption"
        verbose_name_plural = "product consumption"

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="product")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="user")
    portion_size = models.FloatField(validators=[MinValueValidator(0)], verbose_name="portion size")
    date = models.DateTimeField(default=timezone.now, verbose_name="date")

    @property
    def footprint(self):
        """Ecological footprint"""
        return self.product.footprint_per_unit * self.portion_size
