from django.test import TestCase
from .models import Tarea
from django.contrib.auth.models import User

class TareaModelTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Crea una tarea de prueba
        self.tarea = Tarea.objects.create(user=self.user, titulo='Tarea de prueba', email='test@example.com', descripcion='Esta es una tarea de prueba')

    def test_crear_tarea(self):
        # Verifica que la tarea se haya creado correctamente
        self.assertEqual(self.tarea.titulo, 'Tarea de prueba')
        self.assertEqual(self.tarea.email, 'test@example.com')
        self.assertEqual(self.tarea.descripcion, 'Esta es una tarea de prueba')
        
        # Verifica que la relación con el usuario sea correcta
        self.assertEqual(self.tarea.user, self.user)

    def test_editar_tarea(self):
        # Edita la tarea
        self.tarea.titulo = 'Tarea editada'
        self.tarea.email = 'edited@example.com'
        self.tarea.descripcion = 'Esta es una tarea editada'
        self.tarea.save()

        # Recupera la tarea de la base de datos después de la edición
        tarea_editada = Tarea.objects.get(pk=self.tarea.pk)

        # Verifica que los cambios se hayan guardado correctamente
        self.assertEqual(tarea_editada.titulo, 'Tarea editada')
        self.assertEqual(tarea_editada.email, 'edited@example.com')
        self.assertEqual(tarea_editada.descripcion, 'Esta es una tarea editada')

    def test_eliminar_tarea(self):
        # Elimina la tarea
        self.tarea.delete()

        # Intenta recuperar la tarea de la base de datos
        tarea_eliminada = Tarea.objects.filter(pk=self.tarea.pk).first()

        # Verifica que la tarea haya sido eliminada correctamente
        self.assertIsNone(tarea_eliminada)

    def test_str_metodo_tarea(self):
        # Verifica que el método __str__ devuelva el título de la tarea
        self.assertEqual(str(self.tarea), 'Tarea de prueba')