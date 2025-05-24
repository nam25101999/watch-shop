from django.shortcuts import render, get_object_or_404
from .models import Brand, Category, Product
from django.shortcuts import render
from .models import Product, Brand, Category
from django.core.paginator import Paginator
from reviews.forms import ReviewForm
from reviews.models import Review
from django.shortcuts import render, get_object_or_404, redirect


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import (
    Product, Brand, Category, WatchType, Style, Dial,
    StrapMaterial, Color, WaterResistance,
    Movement, Glass, CaseDiameter, SpecialEdition,
    DialShape, Feature, Origin, SortOrder
)

def product_list(request):
    products = Product.objects.all()

    # Lấy dữ liệu bộ lọc
    brands = Brand.objects.all()
    categories = Category.objects.all()
    watch_types = WatchType.objects.all()
    styles = Style.objects.all()
    dials = Dial.objects.all()
    strap_materials = StrapMaterial.objects.all()
    colors = Color.objects.all()
    water_resistances = WaterResistance.objects.all()
    movements = Movement.objects.all()
    glasses = Glass.objects.all()
    case_diameters = CaseDiameter.objects.all()
    special_editions = SpecialEdition.objects.all()
    dial_shapes = DialShape.objects.all()
    features = Feature.objects.all()
    origins = Origin.objects.all()
    sort_orders = SortOrder.objects.all()

    # --- Áp dụng các bộ lọc ---
    brand_id = request.GET.get('brand')
    if brand_id:
        products = products.filter(brand_id=brand_id)

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    gender = request.GET.get('gender')
    if gender:
        products = products.filter(gender=gender)

    min_price = request.GET.get('min_price')
    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            pass

    max_price = request.GET.get('max_price')
    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            pass

    watch_type_id = request.GET.get('watch_type')
    if watch_type_id:
        products = products.filter(watch_type_id=watch_type_id)

    style_id = request.GET.get('style')
    if style_id:
        products = products.filter(style_id=style_id)

    dial_id = request.GET.get('dial')
    if dial_id:
        products = products.filter(dial_id=dial_id)

    strap_material_id = request.GET.get('strap_material')
    if strap_material_id:
        products = products.filter(strap_material_id=strap_material_id)

    color_id = request.GET.get('color')
    if color_id:
        products = products.filter(color_id=color_id)

    water_resistance_id = request.GET.get('water_resistance')
    if water_resistance_id:
        products = products.filter(water_resistance_id=water_resistance_id)

    # Bộ lọc mới
    movement_id = request.GET.get('movement')
    if movement_id:
        products = products.filter(movement_id=movement_id)

    glass_id = request.GET.get('glass')
    if glass_id:
        products = products.filter(glass_id=glass_id)

    case_diameter_id = request.GET.get('case_diameter')
    if case_diameter_id:
        products = products.filter(case_diameter_id=case_diameter_id)

    special_edition_id = request.GET.get('special_edition')
    if special_edition_id:
        products = products.filter(special_edition_id=special_edition_id)

    dial_shape_id = request.GET.get('dial_shape')
    if dial_shape_id:
        products = products.filter(dial_shape_id=dial_shape_id)

    feature_id = request.GET.get('feature')
    if feature_id:
        products = products.filter(feature_id=feature_id)

    origin_id = request.GET.get('origin')
    if origin_id:
        products = products.filter(origin_id=origin_id)

    sort_order_id = request.GET.get('sort_order')
    if sort_order_id:
        products = products.order_by('sort_order__order')  # hoặc các kiểu khác tùy ý

    # --- Sắp xếp mặc định và các tùy chọn khác ---
    sort = request.GET.get('sort')
    if sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    # --- Phân trang ---
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
        'movements': movements,
        'glasses': glasses,
        'case_diameters': case_diameters,
        'special_editions': special_editions,
        'dial_shapes': dial_shapes,
        'features': features,
        'origins': origins,
        'sort_orders': sort_orders,
        'request': request,  # để dùng lại GET trong template
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    extra_images = product.images.all()

    # Lấy danh sách review đã phân trang (5 review/trang)
    reviews_list = Review.objects.filter(product=product).order_by('-created_at')
    paginator = Paginator(reviews_list, 5)
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # hoặc trang login của bạn
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            # Redirect về chính trang chi tiết sản phẩm (để tránh resubmission form)
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'extra_images': extra_images,
        'reviews': reviews,
        'form': form,
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

from django.core.paginator import Paginator

def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews_list = product.reviews.all().order_by('-created_at')

    paginator = Paginator(reviews_list, 5)  # 5 đánh giá 1 trang
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    # Nếu muốn hiển thị form thêm đánh giá trong cùng trang
    if request.user.is_authenticated:
        form = ReviewForm()
    else:
        form = None

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
    })

