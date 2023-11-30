from django.shortcuts import render,redirect
from .models import Product, Brand, Category
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
from django.urls import reverse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.
@cache_page(60*2)
def product_list(request):
    products = Product.objects.all()
    return render(request,'products/product_list_test.html',{'products':products})

# def product_list(request):
#     if cache.get(['products']) is None:
#         products = Product.objects.all()
#         cache.set('products',products)
#     return render(request, "products/product_list_test.html", {"products": products})


class Product_List(ListView):
    model = Product
    paginate_by = 100


class Product_Detail(DetailView):
    model = Product


class BrandList(ListView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context


def add_review (request,id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()
            return redirect(reverse('products:product_detail',kwargs={'id':id}))
        



class CategoryList(ListView):
    model = Category
    paginate_by = 10
