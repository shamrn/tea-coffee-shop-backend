from typing import Union

from django.db import models
from django.utils.translation import gettext_lazy as _

from extension.models import BaseMixin, SortableMixin


class Category(BaseMixin, SortableMixin):
    """Category model"""

    class TypeChoice(models.IntegerChoices):
        """Type choice"""

        COFFEE: int = 0, _('Coffee')
        TEA: int = 1, _('Tea')

    type = models.PositiveSmallIntegerField(choices=TypeChoice.choices, db_index=True,
                                            verbose_name=_('Type product'))
    name = models.CharField(max_length=32, verbose_name=_('Name'))

    def __str__(self):
        """Implement str dunder"""

        return self.name

    class Meta:
        """Meta class"""

        ordering = ['sorting']
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ProductQuerySet(models.QuerySet):
    """Query set for `Product` model"""

    def is_active(self) -> Union['ProductQuerySet', models.QuerySet]:
        """Filter by is active"""

        return self.filter(is_active=True)

    def prefetch_main_product_image(self) -> Union['ProductQuerySet', models.QuerySet]:
        """Prefetch with main `ProductImage` model"""

        return self.prefetch_related(
            models.Prefetch(
                queryset=ProductImage.objects.annotate_min_sorting_value(),
                lookup='product_images',
                to_attr='_product_main_image_prefetched'
            )
        )


class Product(BaseMixin, SortableMixin):
    """Product model"""

    category = models.ManyToManyField(to=Category, related_name='category_products',
                                      verbose_name=_('Categories'))
    name = models.CharField(max_length=100, verbose_name=_('Name'), db_index=True)
    description = models.TextField(verbose_name=_('Description'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Price'))
    volume = models.FloatField(_('Volume'), null=True)

    is_hit = models.BooleanField(default=False, db_index=True,
                                 verbose_name=_('Is hit'))
    is_new = models.BooleanField(default=False, db_index=True,
                                 verbose_name=_('Is new'))
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name=_('Is active'),
                                    help_text=_('If unchecked, the product will not be displayed'))

    objects = models.Manager.from_queryset(ProductQuerySet)()

    def __str__(self):
        """Implement str dunder"""

        return self.name

    class Meta:
        """Meta class"""

        ordering = ['sorting']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    @property
    def image(self):
        """Return main image"""

        if hasattr(self, '_product_main_image_prefetched'):
            return getattr(next(iter(self._product_main_image_prefetched), None), 'image', None)

        return getattr(self.product_images.first(), 'image', None)

    @property
    def product_main_image_prefetched(self) -> 'ProductImage':
        """Return `ProductImage` queryset"""

        if hasattr(self, '_product_main_image_prefetched'):
            return self._product_main_image_prefetched

        return self.product_images.all()


class ProductImageQuerySet(models.QuerySet):
    """Query set 'ProductImage' model"""

    def annotate_min_sorting_value(self) -> Union['ProductImageQuerySet', models.QuerySet]:
        """Annotate min sorting value"""

        return (self.annotate(min_sorting_value=models.Min('product__product_images__sorting'))
                .filter(sorting=models.F('min_sorting_value')))


class ProductImage(BaseMixin, SortableMixin):
    """Product Image model"""

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                related_name='product_images',
                                verbose_name=_('Product image'))
    image = models.ImageField(_('Image'))

    objects = models.Manager.from_queryset(ProductImageQuerySet)()

    def __str__(self):
        """Implement str dunder"""

        return f'%s: {self.id}' % _('Entry number')

    class Meta:
        """Meta class"""

        ordering = ['sorting']
        verbose_name = _('product image')
        verbose_name_plural = _('product images')
