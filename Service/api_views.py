from rest_framework import viewsets

from Service.models import Article
from Service.serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
