from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.TextField(null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_title = models.CharField(max_length=150, verbose_name="Продукт")
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'