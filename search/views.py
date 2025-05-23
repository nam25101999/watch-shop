from django.shortcuts import render
from products.models import Product

def search_products(request):
    query = request.GET.get('q')  # Lấy từ khóa tìm kiếm từ query param q
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)  # Tìm sản phẩm có tên chứa query (không phân biệt hoa thường)

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search/search_results.html', context)
