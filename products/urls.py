from django.urls import path,include
# from .api import product_list_api,product_detail
from .api import ProductDetail,ProductList,CategoryListAPI,CategoryDetail,BrandListApi,BrandDetail,ProductViewSet
# from .views import (
#     Product_List,
#     Product_Detail,
#     BrandList,
#     BrandDetail,
#     CategoryList,
#     product_list,
# )

from rest_framework import routers

router = routers.DefaultRouter()
router.register('myproducts',ProductViewSet)


app_name = "products"


urlpatterns = [
    # path("testing/", product_list),
    # path("", Product_List.as_view(), name="product_list"),
    # path("brands/", BrandList.as_view(), name="brand_list"),
    # path("category/", CategoryList.as_view(), name="category_list"),
    # path("<int:pk>", Product_Detail.as_view(), name="product_detail"),
    # path("brands/<int:pk>", BrandDetail.as_view(), name="brand_detail"),


    # path('api/list/',product_list_api),
    # path('api/list/<int:id>',product_detail),


    path('api/list/cbv/',ProductList.as_view()),
    path('api/list/cbv/<int:pk>',ProductDetail.as_view()),

    path('api/category/',CategoryListAPI.as_view()),
    path('api/brand/',BrandListApi.as_view()),
    path('api/category/<int:pk>/',CategoryDetail.as_view()),
    path('api/brand/<int:pk>/',BrandDetail.as_view()),

    path("myapi/",include(router.urls)),
]
