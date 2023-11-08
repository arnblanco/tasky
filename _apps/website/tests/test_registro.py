from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'mypassword123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view_get(self):
        response = self.client.get(reverse('auth:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/login.html')

    def test_login_view_post(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(reverse('auth:login'), data)
        self.assertEqual(response.status_code, 302) 
        user = User.objects.get(username=self.username)
        self.assertEqual(self.client.session['_auth_user_id'], str(user.id))