from django.contrib import admin
from .models import Product,ProductImages,ProductReview,Brand,Category
# Register your models here.
admin.site.register(ProductReview)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Category)