from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    latest_products = Product.objects.order_by('-id')[:10]
    return render(request, 'index.html', {
        'products' : products,
        'categories':categories,
        'latest_products':latest_products,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    related_products = Product.objects.filter(
        Q(category=product.category) | Q(price__range=(product.price - 10, product.price + 10))
    ).exclude(pk=product_id)[:4]

    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products
        })

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    return render(request, 'category_detail.html', {'category': category, 'products': products})



def dashboard(request):
    return render(request, 'admin/dashboard.html')