from django.shortcuts import render
from .models import Products
def product(request):
    return render(request,'products/product.html')
def products(request):
    return render(request,'products/products.html', {'pro':Products.objects.filter()})