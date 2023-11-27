from rest_framework import serializers
from .models import Product,Brand,Category



class BrandSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()

  class Meta:
    model = Brand
    fields = ['name','image','category']



class CategorySerializer (serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ['name','image']



class ProductSerializer(serializers.ModelSerializer):

  brand = BrandSerializer()
  category = CategorySerializer()

  price_with_discount = serializers.SerializerMethodField()

  # brand = serializers.StringRelatedField()
  # category = serializers.StringRelatedField()

  def get_price_with_discount (self,product):
    return product.price - (product.price * .10)
  



  class Meta:
    model = Product
    fields = '__all__'







class CategoryDetailSerializer (serializers.ModelSerializer):
  products = ProductSerializer(source = 'product_category',many = True)
  class Meta:
    model = Category
    fields = ['name','image','products']


class BrandDetailSerializer (serializers.ModelSerializer):
  products = ProductSerializer(source = 'product_brand',many = True)
  category = serializers.StringRelatedField()

  class Meta:
    model = Brand
    fields = ['name','image','category','products']





    