from django.shortcuts import render , redirect
from shop.models import Product , Category
from .forms import ProductForm, CategoryForm
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


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'product/create.html', {'form': form})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'category/create.html', {'form': form})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/update.html', {'form': form})


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product-list')
    
        
    

def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/update.html', {'form': form})


def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category-list')
   
        
        
    