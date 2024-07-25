from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Category, Product

# Create your views here.

def category_list(request):
    categories = Category.object.all()
    data = [{"id": category.id, "name": category.name} for category in categories]
    return JsonResponse(data, safe=False)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = {"id": category.id, "name": category.name}
    return JsonResponse(data)

def product_list(request):
    products = Product.objects.all()
    data = [
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "description": product.description,
            "category": product.category.name,
            "image": product.image.url if product.image else None
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "description": product.description,
            "category": product.category.name,
            "image": product.image.url if product.image else None
        }
        
    return JsonResponse(data, safe=False)