from django.conf import settings
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Autor',
    )
    published = models.BooleanField(default=False, verbose_name='Publicado')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        permissions = [
            ('publish_article', 'Puede publicar articulos'),
            ('feature_article', 'Puede destacar articulos'),
        ]

    def __str__(self):
        return self.title
