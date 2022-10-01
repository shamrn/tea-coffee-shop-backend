from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from extension.views import AllowAnyMixin, SerializerClassMapperViewSetMixin
from product.models import Category, Product
from product.serializers import CategoryBaseSerializer, ProductListSerializer


class CategoryListViewSet(AllowAnyMixin, ListModelMixin, GenericViewSet):
    """Resource for List category"""

    serializer_class = CategoryBaseSerializer
    queryset = Category.objects.all()


class ProductListViewSet(AllowAnyMixin, SerializerClassMapperViewSetMixin, ListModelMixin):
    """Resource for List product"""

    serializer_class_mapper = {
        'list': ProductListSerializer,
    }

    def get_queryset(self):
        """An overridden `get_queryset` method"""

        queryset = Product.objects.is_active()

        if self.action == 'list':
            return queryset.prefetch_main_product_image()
