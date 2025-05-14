from django.urls import path
from .create_order.views import CreateOrder
from .get_order.views import GetOrderItemAll

urlpatterns = [
    path('order/create/', CreateOrder.as_view(), name='order-create'),
    path('order/get/', GetOrderItemAll.as_view(), name='order-create'),
]
