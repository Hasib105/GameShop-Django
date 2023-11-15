from django.shortcuts import render
from shop.models import Product , Category
# Create your views here.

def dashboard(request):
    return render(request, 'admin/dashboard.html')



def product_list(requset):
    products = Product.objects.order_by('-id')

    return render(requset, 'product/product_list.html',
    {
        'products':products
    })


def category_list(requset):
    categories = Category.objects.order_by('-id')
    
    return render(requset, 'category/category_list.html',
    {
        'categories':categories
    })