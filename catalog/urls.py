from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('product_detail/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', views.ProductCreateView.as_view(), name='create'),
    path('catalog/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('catalog/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),

]
