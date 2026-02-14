from django.contrib import admin
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'views_count')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')