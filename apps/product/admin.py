from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin

from product.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Admin interface for `Category` model"""

    list_display = ('name', 'sorting',)


class ProductImageAdmin(SortableInlineAdminMixin, admin.TabularInline):
    """Admin inline section for model `ProductImage`"""

    model = ProductImage
    extra = 1
    classes = ['collapse']


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Admin interface for `Product` model"""

    list_display = ('id', 'name', 'price', 'is_hit', 'is_new', 'is_active', 'sorting')
    inlines = [ProductImageAdmin]
