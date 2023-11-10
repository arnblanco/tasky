"""Website Registro test case"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegistrationViewTest(TestCase):
    """Registration test case"""

    def test_registration_view_get(self):
        """Registro get method test"""
        response = self.client.get(reverse('auth:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/signup.html')

    def test_registration_view_post(self):
        """Registro post method test"""
        data = {
            'username': 'testuser',
            'password1': 'mypassword123',
            'password2': 'mypassword123'
        }
        response = self.client.post(reverse('auth:signup'), data)
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_registration_view_post_invalid(self):
        """Registro post method invalid test"""
        data = {
            'username': 'testuser',
            'password1': 'mypassword123',
            'password2': 'differentpassword'
        }
        response = self.client.post(reverse('auth:signup'), data)
        self.assertEqual(response.status_code, 200)
