from django.urls import path
from .create_order.views import CreateOrder
from .get_order.views import GetOrderItemAll
from .get_revenue.views import GetRevenue

urlpatterns = [
    path('order/create/', CreateOrder.as_view(), name='order-create'),
    path('order/get/', GetOrderItemAll.as_view(), name='order-list'),
    path('revenue/get/', GetRevenue.as_view(), name = 'revenue')
]
