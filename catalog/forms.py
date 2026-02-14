from django import forms
from django.core.exceptions import ValidationError
from .models import Product

# Список запрещённых слов (в нижнем регистре для сравнения)
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_title', 'description', 'category_name', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'first_name'
        self.fields['product_title'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'last_name'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите фамилию'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'email'
        self.fields['category_name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите email'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'enrollment_date'
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'type': 'date'  # Указание типа поля как даты
        })

    def clean_name(self):
        name = self.cleaned_data.get('product_title')
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError(f'Название содержит запрещённое слово: "{word}".')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError(f'Описание содержит запрещённое слово: "{word}".')
        return description

