from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Product


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'type', 'icon')
    list_filter = ('type',)
    search_fields = ('name',)
