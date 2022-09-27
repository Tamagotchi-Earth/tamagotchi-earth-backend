from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from common.models import ModelBase
from common.utils import UUIDFilenameGenerator


class CustomUser(ModelBase, AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    # This model pretty much copies AbstractUser but without first and last name

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator], verbose_name="username")
    email = models.EmailField(blank=True, verbose_name="email address")
    is_staff = models.BooleanField(default=False, verbose_name="staff status")
    is_active = models.BooleanField(default=True, verbose_name="active")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="date joined")
    name = models.CharField(max_length=255, blank=True, verbose_name="name")
    avatar = models.ImageField(upload_to=UUIDFilenameGenerator(basepath='avatars'), blank=True, null=True,
                               verbose_name="profile picture")

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
