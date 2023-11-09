from django.test import TestCase
from django.urls import reverse
from .models import Tarea
from django.contrib.auth.models import User

class TareaViewTestCase(TestCase):
    def setUp(self):
        # Crea un usuario para la autenticación
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_listar_tareas(self):
        # Crea una tarea de prueba
        Tarea.objects.create(user=self.user, titulo='Tarea de prueba', email='test@example.com', descripcion='Esta es una tarea de prueba')
        
        # Realiza una solicitud GET a la vista de listar tareas
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tarea'))

        # Verifica que la respuesta sea exitosa y que la tarea creada esté presente en la página
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarea de prueba')

    def test_agregar_tarea(self):
        # Realiza una solicitud POST para agregar una tarea
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('tarea'), {'titulo': 'Nueva Tarea', 'email': 'nueva@example.com', 'descripcion': 'Descripción de la nueva tarea'})

        # Verifica que la tarea se haya creado correctamente y que la vista redirija a la página de listado de tareas
        self.assertEqual(response.status_code, 302)  # Código 302 indica una redirección

        # Verifica que la tarea creada esté presente en la lista
        response = self.client.get(reverse('tarea'))
        self.assertContains(response, 'Nueva Tarea')
