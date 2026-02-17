from .models import Category, Product
from django.http import Http404

class ProductFilter:
    @staticmethod
    def filter_by_category(category_name):
        try:
            category = Category.objects.get(category_name=category_name)
        except Category.DoesNotExist:
            raise Http404("Категория не найдена")
        products = Product.objects.filter(category_name=category, is_published=True)
        if not products.exists():
            return Product.objects.none()
        return products