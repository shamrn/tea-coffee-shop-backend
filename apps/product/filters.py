from django.core.validators import EMPTY_VALUES
from django_filters import rest_framework as filters

from product.models import Product


class ProductFilterSet(filters.FilterSet):
    """Product filter set"""

    search = filters.CharFilter(method='by_annotate_similarity', help_text='Search product')
    type = filters.CharFilter(field_name='category__type')

    class Meta:
        """Meta class"""

        model = Product
        fields = ('category', 'type')

    @staticmethod
    def by_annotate_similarity(queryset, name: str, value: str):  # NOQA
        """Method returns filtered queryset"""

        if value not in EMPTY_VALUES:
            return queryset.annotate_trigram_similarity(value).filter(trigram_similarity__gt=0.3)

        return queryset.none()
