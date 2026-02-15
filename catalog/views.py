from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView, DeleteView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProductForm

# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name =  'catalog/product_detail.html'
    context_object_name = 'product'  # имя переменной в шаблоне
    pk_url_kwarg = 'product_id'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
