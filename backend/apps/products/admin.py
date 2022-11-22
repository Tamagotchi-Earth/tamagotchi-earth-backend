from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Product, UserProductConsumption


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'type', 'icon')
    list_filter = ('type',)
    search_fields = ('name',)


@admin.register(UserProductConsumption)
class UserProductConsumptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'portion_size', 'date')
    ordering = ('-date',)
