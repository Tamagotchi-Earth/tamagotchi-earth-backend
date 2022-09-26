from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import ModelBase
from common.utils import UUIDFilenameGenerator


class CustomUser(ModelBase, AbstractUser):
    """Custom user model"""

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    # Manually remove first_name and last_name from AbstractUser
    first_name = None
    last_name = None
    name = models.CharField(max_length=255, blank=True, verbose_name="Name")
    avatar = models.ImageField(upload_to=UUIDFilenameGenerator(basepath='avatars'), blank=True, null=True,
                               verbose_name="Profile picture")
