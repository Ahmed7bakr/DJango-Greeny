from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import generics





# @api_view(['GET'])
# def product_list_api (request):
#   products = Product.objects.all()[:10]
#   data = ProductSerializer(products, many = True).data
#   return Response({'success':True,'Product List':data})


# @api_view(['GET'])
# def product_detail (request,id):
#   products = Product.objects.get(id=id)
#   data = ProductSerializer(products).data
#   return Response({'success':True,'Product':data})


class ProductList (generics.ListCreateAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()


class ProductDetail (generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()

