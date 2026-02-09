from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавляет тестовые категории и продукты, предварительно очищая базу'

    def handle(self, *args, **options):
        # Удаляем все данные из Product и Category
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем тестовые категории
        categories = [
            Category.objects.create(category_name='Фрукты', description='Свежие фрукты'),
            Category.objects.create(category_name='Овощи', description='Свежие овощи'),
        ]

        # Создаем тестовые продукты
        products = [
            Product.objects.create(product_title='Яблоко', description='Красное яблоко', category_name=categories[0], price=50),
            Product.objects.create(product_title='Морковь', description='Оранжевая морковь', category_name=categories[1], price=30),
        ]

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены.'))