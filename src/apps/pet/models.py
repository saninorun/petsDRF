from django.db import models

class ProductBD(models.Model):
	title = models.CharField(max_length=255)
	accounting_unit = models.CharField(max_length=20)
	product_category = models.CharField(max_length=40)
	manufacturer = models.CharField(max_length=255)
	article_number = models.IntegerField()
    
	def __str__(self):
		return self.title
	
class UserBD(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	
	def __str__(self):
		return self.title

class DiscountBD(models.Model):
	date_start = models.DateTimeField()
	date_stop = models.DateTimeField()
	discount = models.PositiveIntegerField()
	product = models.ForeignKey(ProductBD, on_delete=models.CASCADE)

class SellPriceBD(models.Model):
	date_start = models.DateTimeField()
	date_stop = models.DateTimeField()
	price = models.FloatField()
	product = models.ForeignKey(ProductBD, on_delete=models.CASCADE)

class OrderBD(models.Model):
	number_order = models.PositiveIntegerField(null=True)
	user = models.ForeignKey(UserBD, on_delete=models.CASCADE)
	date = models.DateTimeField()

	def __str__(self) -> str:
		return self.number_order

class OrderitemBD(models.Model):
	order = models.ForeignKey(OrderBD, on_delete=models.CASCADE, related_name='items_list')
	product = models.ForeignKey('ProductBD', on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	sell_price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField(null=True, blank=True)
	total = models.FloatField()
	
class StockOrderBD(models.Model):
	manager = models.ForeignKey(UserBD, on_delete=models.CASCADE)
	date = models.DateTimeField()
	
class StockOrderItemBD(models.Model):
	stock_order = models.ForeignKey(StockOrderBD, on_delete=models.CASCADE, related_name='stockitem_list')
	quantity = models.PositiveIntegerField()
	purchase_price = models.PositiveIntegerField()
	product = models.ForeignKey(ProductBD, on_delete=models.CASCADE)
