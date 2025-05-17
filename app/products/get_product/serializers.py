from rest_framework import serializers
from products.models.products import Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    brand_logo = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'sku', 'barcode', 'description',
            'category', 'category_name',
            'brand', 'brand_name', 'brand_logo',
            'price', 'cost_price', 'discount_price',
            'inventory_quantity', 'low_stock_threshold', 'unit',
            'is_active', 'is_featured',
            'image', 'image_url',
            'created_at', 'updated_at'
        ]

    def get_brand_logo(self, obj):
        return obj.brand.logo.url if obj.brand and obj.brand.logo else None

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None

    def validate(self, data):
        pass