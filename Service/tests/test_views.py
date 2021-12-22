from http import HTTPStatus

from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils import timezone

from Service.models import Article


class HomeViewTestCase(SimpleTestCase):

    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_app_name(self):
        response = self.client.get(reverse('Service:home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Service:home'))
        self.assertTemplateUsed(response, 'service/home.html')


class AboutViewTestCase(SimpleTestCase):

    def test_url_exists(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_app_name(self):
        response = self.client.get(reverse('Service:about'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Service:about'))
        self.assertTemplateUsed(response, 'service/about.html')


class ContactViewTestCase(SimpleTestCase):

    def test_url_exists(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_app_name(self):
        response = self.client.get(reverse('Service:contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Service:contact'))
        self.assertTemplateUsed(response, 'service/contact.html')


class FaqViewTestCase(SimpleTestCase):

    def test_url_exists(self):
        response = self.client.get('/faq')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_app_name(self):
        response = self.client.get(reverse('Service:faq'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Service:faq'))
        self.assertTemplateUsed(response, 'service/faq.html')


class LatestUpdateViewTestCase(SimpleTestCase):

    def test_url_exists(self):
        response = self.client.get('/latest-update')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_app_name(self):
        response = self.client.get(reverse('Service:latest-update'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Service:latest-update'))
        self.assertTemplateUsed(response, 'service/latest-update.html')


class AdminViewTestCase(SimpleTestCase):

    def test_url_exists(self):
        response = self.client.get('/admin-manager')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_app_name(self):
        response = self.client.get(reverse('Service:admin'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Service:admin'))
        self.assertTemplateUsed(response, 'service/admin.html')


class UploadTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'topic': 'Lorem ipsum',
            'article': 'Lorem ipsum',
            'date': timezone.now()
        }

    def test_url_exists(self):
        response = self.client.post('/admin-manager/upload', data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_accessible_by_app_name(self):
        response = self.client.post(reverse('Service:upload'), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_view_redirects_if_successful(self):
        response = self.client.post(reverse('Service:upload'), data=self.data)
        self.assertRedirects(response, reverse('Service:admin'))
