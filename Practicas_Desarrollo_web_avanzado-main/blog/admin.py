from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published', 'created_at')
	list_filter = ('published', 'created_at')
	search_fields = ('title', 'content', 'author__username')
