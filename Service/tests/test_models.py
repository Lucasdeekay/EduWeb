from django.test import TestCase
from django.utils import timezone

from Service.models import Article


class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(topic='Topic', article='Lorem ipsum', date=timezone.now())

    def test_topic_label(self):
        article = Article.objects.get(topic='Topic')
        field_label = article._meta.get_field('topic').verbose_name
        self.assertEqual(field_label, 'topic')

    def test_topic_max_length(self):
        article = Article.objects.get(topic='Topic')
        max_length = article._meta.get_field('topic').max_length
        self.assertEqual(max_length, 50)

    def test_article_label(self):
        article = Article.objects.get(topic='Topic')
        field_label = article._meta.get_field('article').verbose_name
        self.assertEqual(field_label, 'article')

    def test_article_max_length(self):
        article = Article.objects.get(topic='Topic')
        max_length = article._meta.get_field('article').max_length
        self.assertEqual(max_length, 250)

    def test_image_label(self):
        article = Article.objects.get(topic='Topic')
        field_label = article._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_date_label(self):
        article = Article.objects.get(topic='Topic')
        field_label = article._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')
