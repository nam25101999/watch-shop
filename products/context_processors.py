from .models import Brand, Category

def menu_processor(request):
    return {
        'brands': Brand.objects.all(),
        'categories': Category.objects.all(),
    }
