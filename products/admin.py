from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'selling_price', 'stock', 'is_active')
    search_fields = ('name', 'category')
    list_filter = ('category', 'is_active')
