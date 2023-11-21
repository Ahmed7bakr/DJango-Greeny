from django.contrib import admin
from .models import Order, OrderDetail, CART, CARTDetail

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CART)
admin.site.register(CARTDetail)
