from django.db import models

class ProductBD(models.Model):
	title = models.CharField(max_length=255)
	accounting_unit = models.CharField(max_length=20)
	product_category = models.CharField(max_length=40)
	manufacturer = models.CharField()
	article_number = models.IntegerField()
    
	def __str__(self):
		return self.title
	
class DiscountBD(models.Model):
	date_start = models.DateTimeField()
	date_stop = models.DateTimeField()
	discount = models.PositiveIntegerField()

class UserBD(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	
class SellPriceBD(models.Model):
	date_start = models.DateTimeField()
	date_stop = models.DateTimeField()
	price = models.FloatField()
	product_id = models.ForeignKey(ProductBD, on_delete=models.CASCADE)
	discount_id = models.ForeignKey(DiscountBD, on_delete=models.CASCADE, null=True)

class OrderBD(models.Model):
	user_id = models.ForeignKey(UserBD, on_delete=models.CASCADE)
	date = models.DateTimeField()


class OrderitemDB(models.Model):
	order_id = models.ForeignKey(OrderBD, on_delete=models.CASCADE)
	stockitem_id = models.PositiveIntegerField()
	sell_price_id = models.ForeignKey(SellPriceBD, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	
class StockOrderDB(models.Model):
	manager_id = models.ForeignKey(UserBD, on_delete=models.CASCADE)
	date = models.DateTimeField()
	
class StockOrderItem(models.Model):
	stock_order_id = models.ForeignKey(StockOrderDB, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	purchase_price = models.PositiveIntegerField()
	product_id = models.ForeignKey(ProductBD, on_delete=models.CASCADE)
