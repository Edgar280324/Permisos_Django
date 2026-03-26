from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm
from .models import Article


@login_required
def article_list(request):
	"""Cualquier usuario autenticado puede ver la lista."""
	articles = Article.objects.select_related('author').all().order_by('-created_at')
	return render(request, 'blog/article_list.html', {'articles': articles})


@permission_required('blog.add_article', raise_exception=True)
def article_create(request):
	"""Solo usuarios con permiso add_article pueden crear."""
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.author = request.user
			article.save()
			messages.success(request, 'Articulo creado correctamente.')
			return redirect('article_list')
	else:
		form = ArticleForm()
	return render(request, 'blog/article_form.html', {'form': form})


@login_required
@permission_required('blog.delete_article', raise_exception=True)
def article_delete(request, pk):
	"""Solo usuarios con permiso delete_article pueden eliminar."""
	article = get_object_or_404(Article, pk=pk)
	if request.method == 'POST':
		article.delete()
		messages.success(request, 'Articulo eliminado correctamente.')
		return redirect('article_list')
	return render(request, 'blog/article_confirm_delete.html', {'article': article})


@permission_required('blog.publish_article', raise_exception=True)
def article_publish(request, pk):
	"""Solo usuarios con permiso personalizado publish_article pueden publicar."""
	article = get_object_or_404(Article, pk=pk)
	article.published = True
	article.save(update_fields=['published'])
	messages.success(request, f'"{article.title}" ha sido publicado.')
	return redirect('article_list')
