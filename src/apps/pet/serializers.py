from rest_framework import serializers

from .models import (
    SellPriceBD, 
    ProductBD, 
    DiscountBD,
    UserBD,
    OrderBD,
    OrderitemBD,
    StockOrderBD,
    StockOrderItemBD,
    )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBD
        fields = ['title', 'accounting_unit', 'product_category', 'manufacturer', 'article_number']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBD
        fields = ['id','name', 'status']

class DiscountSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = DiscountBD
        fields = ['product', 'discount', 'date_start', 'date_stop']
     
class SellPriceSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = SellPriceBD
        fields = ['product', 'price', 'date_start', 'date_stop']

class OrderitemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderitemBD
        fields = ['product', 'sell_price', 'discount', 'quantity', 'total']
        
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items_list = OrderitemSerializer(many=True)
    class Meta:
        model = OrderBD
        fields = ['user', 'date', 'items_list']

class StockOrderSerializer(serializers.ModelSerializer):
    manager = UserSerializer()
    class Meta:
        model = StockOrderBD
        fields = ['manager','date']

class StockOrderItemSerializer(serializers.ModelSerializer):
    stock_order = StockOrderSerializer()
    product = ProductSerializer()
    class Meta:
        model = StockOrderItemBD
        fields = ['stock_order', 'product', 'quantity', 'purchase_price']