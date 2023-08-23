from django.contrib import admin
from .models import Product,ProductImages,ProductReview,Brand,Category


# Register your models here.

class ProductImageTabular (admin.TabularInline):
    model = ProductImages


class ProductAdmin (admin.ModelAdmin):
    inlines=[ProductImageTabular]
    list_display=['name','price','flag','quantity']
    list_filter=['flag','category','brand']
    search_fields=['name','subtitle','desc']



admin.site.register(ProductReview)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Category)