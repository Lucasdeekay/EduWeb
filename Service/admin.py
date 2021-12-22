from django.contrib import admin

from Service.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('topic', 'article', 'image', 'date')


admin.site.register(Article, ArticleAdmin)
