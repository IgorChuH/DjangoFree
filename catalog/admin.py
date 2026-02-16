from django.contrib import admin
from .models import Product, Category
from users.models import CustomUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'price', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('product_title', 'description')

@admin.register(CustomUser)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ('password',)