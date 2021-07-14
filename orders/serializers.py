from rest_framework import serializers
from .models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    product_order_product = OrderProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'date', 'total_price', 'address', 'status', 'product_order_product')
