from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from extension.pagination import LimitOffsetPaginationMixin
from extension.views import AllowAnyMixin, SerializerClassMapperViewSetMixin
from product import filters
from product.models import Category, Product
from product.serializers import CategoryBaseSerializer, ProductListSerializer


class CategoryListViewSet(AllowAnyMixin, ListModelMixin, GenericViewSet):
    """Resource for List category"""

    serializer_class = CategoryBaseSerializer
    queryset = Category.objects.all()


class ProductListViewSet(AllowAnyMixin,
                         LimitOffsetPaginationMixin,
                         SerializerClassMapperViewSetMixin,
                         ListModelMixin):
    """Resource for List product"""

    serializer_class_mapper = {
        'list': ProductListSerializer,
    }

    filter_class = filters.ProductFilterSet

    def get_queryset(self):
        """An overridden `get_queryset` method"""

        return Product.objects.is_active().prefetch_main_product_image()
