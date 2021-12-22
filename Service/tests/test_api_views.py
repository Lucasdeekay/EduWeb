from http import HTTPStatus

from rest_framework.test import APITestCase


class ArticleAPIViewTest(APITestCase):

    def test_article_api_url_exists(self):
        response = self.client.get('/api/article/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
