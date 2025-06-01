from django.db import models
from django.core.exceptions import ValidationError
from products.models import Product
from .wareHouse import Warehouse
from .supplier import Supplier

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reserved_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reorder_point = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    safety_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reorder_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    batch_number = models.CharField(max_length=100, null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.CharField(max_length=50, default='unit')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventory'
        unique_together = ('product', 'warehouse', 'batch_number')

    def clean(self):
        if self.quantity < 0 or self.available_quantity < 0 or self.reserved_quantity < 0:
            raise ValidationError("Quantities cannot be negative.")

    def __str__(self):
        return f"{self.product.name} - {self.quantity} {self.unit} at {self.warehouse.name}"