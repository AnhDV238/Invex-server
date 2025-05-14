from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'Order {self.order_number}'
