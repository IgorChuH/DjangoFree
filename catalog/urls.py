from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

]
