from rest_framework.routers import SimpleRouter

from product import views

app_name = 'product'

product_router = SimpleRouter()

product_router.register('', views.ProductListViewSet, basename='product')
product_router.register('categories', views.CategoryListViewSet, basename='categories')

urlpatterns = (
    product_router.urls
)
