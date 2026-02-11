from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавляет тестовые категории и продукты, предварительно очищая базу'

    def handle(self, *args, **options):
        # Удаляем все данные из Product и Category
        Product.objects.all().delete()
        Category.objects.all().delete()
