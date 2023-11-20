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
from django.contrib import admin


admin.site.register(SellPriceBD)
admin.site.register(ProductBD)
admin.site.register(DiscountBD)
admin.site.register(UserBD)
admin.site.register(OrderBD)
admin.site.register(OrderitemBD)
admin.site.register(StockOrderBD)
admin.site.register(StockOrderItemBD)

