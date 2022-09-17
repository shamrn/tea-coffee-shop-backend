from rest_framework import serializers

from product.models import Category


class CategoryBaseSerializer(serializers.ModelSerializer):
    """Category base serializer"""

    class Meta:
        """Meta class"""

        model = Category
        fields = ['id', 'name']
