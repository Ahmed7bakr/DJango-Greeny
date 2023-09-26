from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail,CategoryList

app_name = 'products'


urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('brands/',BrandList.as_view(),name='brand_list'),
    path('category/',CategoryList.as_view(),name='category_list'),
    path('<int:pk>',ProductDetail.as_view(),name='product_detail'),
    path('brands/<int:pk>',BrandDetail.as_view(),name='brand_detail'),
]
