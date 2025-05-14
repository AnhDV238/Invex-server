from django.db import models
from .category import Category
from .brand import Brand
from cloudinary.models import CloudinaryField # type: ignore

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=100, unique=True)
    barcode = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    inventory_quantity = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=5)
    unit = models.CharField(max_length=50, default='cái')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
    def __str__(self):
            return self.name
