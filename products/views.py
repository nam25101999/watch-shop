from django.shortcuts import render, get_object_or_404
from .models import Brand, Category, Product
from django.shortcuts import render
from .models import Product, Brand, Category
from django.core.paginator import Paginator

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Brand, Category, WatchType, Style, Dial, StrapMaterial, Color, WaterResistance

def product_list(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    watch_types = WatchType.objects.all()
    styles = Style.objects.all()
    dials = Dial.objects.all()
    strap_materials = StrapMaterial.objects.all()
    colors = Color.objects.all()
    water_resistances = WaterResistance.objects.all()

    # Lọc theo các trường cơ bản
    if brand_id := request.GET.get('brand'):
        products = products.filter(brand_id=brand_id)

    if category_id := request.GET.get('category'):
        products = products.filter(category_id=category_id)

    if gender := request.GET.get('gender'):
        products = products.filter(gender=gender)

    if min_price := request.GET.get('min_price'):
        products = products.filter(price__gte=min_price)

    if max_price := request.GET.get('max_price'):
        products = products.filter(price__lte=max_price)

    # Lọc theo các trường mở rộng
    if watch_type_id := request.GET.get('watch_type'):
        products = products.filter(watch_type_id=watch_type_id)

    if style_id := request.GET.get('style'):
        products = products.filter(style_id=style_id)

    if dial_id := request.GET.get('dial'):
        products = products.filter(dial_id=dial_id)

    if strap_material_id := request.GET.get('strap_material'):
        products = products.filter(strap_material_id=strap_material_id)

    if color_id := request.GET.get('color'):
        products = products.filter(color_id=color_id)

    if water_resistance_id := request.GET.get('water_resistance'):
        products = products.filter(water_resistance_id=water_resistance_id)

    # Sắp xếp
    sort = request.GET.get('sort')
    if sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    # Phân trang
    paginator = Paginator(products, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'brands': brands,
        'categories': categories,
        'watch_types': watch_types,
        'styles': styles,
        'dials': dials,
        'strap_materials': strap_materials,
        'colors': colors,
        'water_resistances': water_resistances,
        'request': request,
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
