from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseMixin(models.Model):
    """Base mixin model"""

    created = models.DateTimeField(default=timezone.now, editable=False,
                                   verbose_name=_('date created'))
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name=_('date updated'))

    class Meta:
        abstract = True


class SortableMixin(models.Model):
    """Sortable mixin model"""

    # Sorting with library sortable2
    sorting = models.PositiveSmallIntegerField(default=0, blank=False, null=False,
                                               verbose_name=_('Sorting'))

    class Meta:
        abstract = True
