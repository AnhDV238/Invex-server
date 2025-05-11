from django.urls import path
from .views import ProductCreateAPIView

urlpatterns = [
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
]
