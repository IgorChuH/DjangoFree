from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView, DeleteView, View
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .forms import ProductForm

# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):
    model = Product # говорим Django, что параметр называется Product_id
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # привязываем текущего пользователя
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, является ли пользователь владельцем или модератором
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.update'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        if 'is_published' in form.changed_data:
            if not self.request.user.has_perm('catalog.can_unpublish_product'):
                form.instance.is_published = self.get_object().is_published
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.delete'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ProductPublicView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для публикации продукта.")
        product.is_published = not product.is_published
        product.save()
        return redirect('catalog:product_detail', pk=product.pk)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
