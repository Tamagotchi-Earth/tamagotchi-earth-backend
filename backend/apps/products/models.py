import uuid
from django.core.validators import MinValueValidator
from django.db import models
from common.models import ModelBase
from common.utils import UUIDFilenameGenerator
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
    hint = models.CharField(max_length=255, blank=False, verbose_name="hint")
    default_portion_size = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True,
                                             verbose_name="default user portion size")

    def __str__(self):
        return str(self.name)
