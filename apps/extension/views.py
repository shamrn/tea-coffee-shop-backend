from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from extension.serializers import EmptySerializer


class AllowAnyMixin:
    """Permission classes mixin"""

    permission_classes = (AllowAny,)


class SerializerClassMapperViewSetMixin(GenericViewSet):
    """ViewSet serializer class mapper mixin."""

    serializer_class_mapper = dict()

    def get_serializer_class(self):
        serializer_class = EmptySerializer

        try:
            action_w_method = f'{self.action}_{self.request.method}'.lower()

            if action_w_method in self.serializer_class_mapper:
                serializer_class = self.serializer_class_mapper[action_w_method]
            elif self.action in self.serializer_class_mapper:
                serializer_class = self.serializer_class_mapper[self.action]
            else:
                serializer_class = super(
                    SerializerClassMapperViewSetMixin, self).get_serializer_class()
        except AssertionError:
            pass
        finally:
            return serializer_class


class SerializerClassMapperAPIViewMixin(GenericAPIView):
    """ViewSet serializer class mapper mixin."""

    serializer_class_mapper = dict()

    def get_serializer_class(self):
        serializer_class = EmptySerializer

        try:
            http_method = self.request.method.lower()

            if http_method in self.serializer_class_mapper:
                serializer_class = self.serializer_class_mapper[http_method]
            else:
                serializer_class = super(
                    SerializerClassMapperAPIViewMixin, self).get_serializer_class()
        except AssertionError:
            pass
        finally:
            return serializer_class
