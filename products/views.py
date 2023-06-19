from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductsForm

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def create_products(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductsForm()
    return render(request, 'create_products.html', {'form': form})

def update_products(request, products_id):
    products = get_object_or_404(Product, pk=products_id)
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductsForm(instance=products)
    return render(request, 'update_products.html', {'form': form, 'products': products})

def delete_products(request, products_id):
    products = get_object_or_404(Product, pk=products_id)
    if request.method == 'POST':
        products.delete()
        return redirect('products_list')
    return render(request, 'delete_products.html', {'products': products})
