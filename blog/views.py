from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Reviews
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Reviews
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)



class BlogDetailView(DetailView):
    model = Reviews
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # Увеличиваем счётчик просмотров при каждом просмотре
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj


class BlogCreateView(CreateView):
    model = Reviews
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Reviews
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = Reviews
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:list')

