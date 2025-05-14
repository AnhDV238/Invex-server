from rest_framework import serializers
from manage_inventory.models import Order
from manage_inventory.models import OrderItem
from products.models import Product
from django.utils.timezone import now

class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class OrderSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)
    note = serializers.CharField(required=False)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Đơn hàng phải có ít nhất 1 sản phẩm.")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        total_price = 0
        order = Order.objects.create(
            order_number=now().strftime("ORD%Y%m%d%H%M%S"),
            total_price=0,
            **validated_data
        )

        for item in items_data:
            product = Product.objects.get(id=item["product_id"])
            price = product.discount_price or product.price
            quantity = item["quantity"]
            total_price += price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )

        order.total_price = total_price
        order.save()
        return order
