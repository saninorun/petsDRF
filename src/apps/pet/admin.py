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
from django.contrib import admin


admin.site.register(SellPriceBD)
admin.site.register(ProductBD)
admin.site.register(DiscountBD)
admin.site.register(UserBD)
admin.site.register(OrderBD)
admin.site.register(OrderitemDB)
admin.site.register(StockOrderDB)
admin.site.register(StockOrderItemDB)

