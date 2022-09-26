from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        ("Данные для авторизации", {'fields': (
            'username',
            'email',
            'password',
            'is_active',
            'is_staff'
        )}),
        ("Личные данные", {'fields': (
            'name',
            'avatar',
        )}),
    )
    list_display = ('username', 'email', 'name')
    ordering = ('-is_staff', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'name')


# Unregister Group model
admin.site.unregister(Group)
# Unregister allauth models
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)
