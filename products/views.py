from django.shortcuts import render, get_object_or_404
from .models import Brand, Category, Product
from django.shortcuts import render
from .models import Product, Brand, Category

def product_list(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    # Bộ lọc
    brand_id = request.GET.get('brand')
    category_id = request.GET.get('category')
    gender = request.GET.get('gender')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if brand_id:
        products = products.filter(brand_id=brand_id)
    if category_id:
        products = products.filter(category_id=category_id)
    if gender:
        products = products.filter(gender=gender)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # Lấy thêm ảnh phụ nếu có
    extra_images = product.images.all()
    context = {
        'product': product,
        'extra_images': extra_images,
    }
    return render(request, 'shop/product_detail.html', context)

def brand_list(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'shop/brand_list.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'shop/category_list.html', context)
