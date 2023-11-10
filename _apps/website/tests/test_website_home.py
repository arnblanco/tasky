"""Website home view test"""
from django.urls import reverse
from django.test import TestCase


class WebsiteHomeViewTestCase(TestCase):
    """Home view test"""

    def test_website_home_view_get(self):
        """Home get method test"""
        response = self.client.get(reverse('website:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')
