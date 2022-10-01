from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationMixin:
    """Limit offset pagination mixin"""

    pagination_class = LimitOffsetPagination
    max_limit = 100
