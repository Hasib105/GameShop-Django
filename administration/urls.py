from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('product_list/', views.product_list, name='product-list' ),
    path('category_list/', views.category_list, name='category-list' ),
]
