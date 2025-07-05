from django.shortcuts import render
from django.db.models import Q
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )

    return render(request, 'products/product_list.html', {'products': products})
