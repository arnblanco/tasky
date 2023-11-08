from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class WebsiteHomeViewTestCase(TestCase):
    def setUp(self):
        return True

    def test_website_home_view_get(self):
        response = self.client.get(reverse('website:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')