from django.db import models


class ModelBase(models.Model):
    """Absract base model class that specifies fields common for all models"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="Дата измерения")
