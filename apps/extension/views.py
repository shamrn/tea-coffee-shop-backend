from rest_framework.permissions import AllowAny


class AllowAnyMixin:
    """Permission classes mixin"""

    permission_classes = (AllowAny, )
