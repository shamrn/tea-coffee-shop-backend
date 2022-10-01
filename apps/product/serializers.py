from rest_framework import serializers

from product.models import Category, Product, ProductImage


class CategoryBaseSerializer(serializers.ModelSerializer):
    """Category base serializer"""

    class Meta:
        """Meta class"""

        model = Category
        fields = ['id', 'name']


class ProductListSerializer(serializers.ModelSerializer):
    """Product base serializer"""

    image = serializers.ImageField()

    class Meta:
        """Meta class"""

        model = Product
        fields = [
            'id',
            'name',
            'volume',
            'price',
            'image'
        ]
