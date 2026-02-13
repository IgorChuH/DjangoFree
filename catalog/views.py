from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name =  'catalog/product_detail.html'
    context_object_name = 'product'  # имя переменной в шаблоне
    pk_url_kwarg = 'product_id'


