from django.db import models
from .order import Order
from products.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # giá bán lúc đó

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
