from rest_framework.response import Response
from .serializers import ProductSerializer,BrandSerializer,CategorySerializer,CategoryDetailSerializer,BrandDetailSerializer
from .models import Product,Brand,Category
from rest_framework.decorators import api_view
from rest_framework import generics
# import django_filters.rest_framework
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets






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
  # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
  filter_backends = [SearchFilter]
  search_fields = ['name']
  permission_classes=[IsAuthenticated]


class ProductDetail (generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()


class CategoryListAPI(generics.ListAPIView):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()


class CategoryDetail (generics.RetrieveAPIView):
  serializer_class = CategoryDetailSerializer
  queryset = Category.objects.all()


class BrandListApi(generics.ListAPIView):
  serializer_class = BrandSerializer
  queryset = Brand.objects.all()


class BrandDetail (generics.RetrieveAPIView):
  serializer_class = BrandDetailSerializer
  queryset = Brand.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()

