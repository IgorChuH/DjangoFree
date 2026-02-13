from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'blog'

urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
]