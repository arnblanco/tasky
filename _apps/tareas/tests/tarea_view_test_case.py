"""Tareas views test case"""
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from _apps.tareas.models import Tarea

class TareaViewTestCase(TestCase):
    """Tareas view cases"""

    def setUp(self):
        """Setup cases"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_listar_tareas(self):
        """Listar tareas cases"""
        Tarea.objects.create(user=self.user, titulo='Tarea de prueba', email='test@example.com', descripcion='Esta es una tarea de prueba')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tarea'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarea de prueba')

    def test_agregar_tarea(self):
        """Agregar tarea cases"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
                            reverse('tarea'),
                            {
                                'titulo': 'Nueva Tarea',
                                'email': 'nueva@example.com',
                                'descripcion': 'Descripción de la nueva tarea'
                            }
                        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('tarea'))
        self.assertContains(response, 'Nueva Tarea')
