from django.contrib import admin
from .models import Product, Category
# Register your models here.

admin.site.register(Category, list_display=('name',))
admin.site.register(Product, list_display=('name', 'price'))