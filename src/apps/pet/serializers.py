from rest_framework import serializers

from .models import (
    SellPriceBD, 
    ProductBD, 
    DiscountBD,
    UserBD,
    OrderBD,
    OrderitemDB,
    StockOrderDB,
    StockOrderItemDB,
    )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBD
        fields = ['title', 'accounting_unit', 'product_category', 'manufacturer', 'article_number']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountBD
        fields = ['date_start', 'date_stop', 'discount']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBD
        fields = ['name', 'status']
     
class SellPriceSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many = True, required = True)
    discount_id = DiscountSerializer(many = True, required = True)

    class Meta:
        model = SellPriceBD
        fields = ['date_start', 'date_stop', 'product_id', 'price', 'discount_id']

class OrderSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = OrderBD
        fields = ['user_id', 'date']

class OrderitemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()
    sell_price_id = SellPriceSerializer()
    class Meta:
        model = OrderitemDB
        fields = ['order_id', 'sell_price_id', 'quantity']

class StockOrderSerializer(serializers.ModelSerializer):
    manager_id = UserSerializer()
    class Meta:
        model = StockOrderDB
        fields = ['manager_id','date']

class StockOrderItemSerializer(serializers.ModelSerializer):
    stock_order_id = StockOrderSerializer()
    product_id = ProductSerializer()
    class Meta:
        model = StockOrderItemDB
        fields = ['stock_order_id', 'product_id', 'quantity', 'purchase_price']