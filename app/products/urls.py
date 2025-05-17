from django.urls import path
from products.create_product.views import ProductCreateAPIView
from products.get_product.views import ProductListAPIView

urlpatterns = [
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/get/', ProductListAPIView.as_view(), name='product-get'),
]
