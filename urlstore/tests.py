from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from .models import UrlStore


class UrlStoreViewSetTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client = APIClient()

    def test_short_url_create(self):
        data = {
            'url': 'https://www.google.com'
        }
        response = self.api_client.post('/u/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        short_url = response.data['short_url']
        self.assertIsNotNone(short_url)
        response = self.api_client.get(f'/u/{short_url}/')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        url_store = UrlStore.objects.get(pk=short_url)
        self.assertEqual(url_store.visit_counter, 1)
