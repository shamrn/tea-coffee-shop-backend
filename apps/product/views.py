from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from extension.views import AllowAnyMixin
from product.models import Category
from product.serializers import CategoryBaseSerializer


class CategoryListSerializer(AllowAnyMixin, ListModelMixin, GenericViewSet):
    """Resource for List category"""

    serializer_class = CategoryBaseSerializer
    queryset = Category.objects.all()
