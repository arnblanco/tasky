"""Tareas model test case"""
from django.contrib.auth.models import User
from django.test import TestCase
from _apps.tareas.models import Tarea


class TareaModelTestCase(TestCase):
    """Tarea model test"""

    def setUp(self):
        """Class setup"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.tarea = Tarea.objects.create(
                                            user=self.user,
                                            titulo='Tarea de prueba',
                                            email='test@example.com',
                                            descripcion='Esta es una tarea de prueba'
                                        )

    def test_crear_tarea(self):
        """Create tarea test"""
        self.assertEqual(self.tarea.titulo, 'Tarea de prueba')
        self.assertEqual(self.tarea.email, 'test@example.com')
        self.assertEqual(self.tarea.descripcion, 'Esta es una tarea de prueba')
        self.assertEqual(self.tarea.user, self.user)

    def test_editar_tarea(self):
        """Edit tarea"""
        self.tarea.titulo = 'Tarea editada'
        self.tarea.email = 'edited@example.com'
        self.tarea.descripcion = 'Esta es una tarea editada'
        self.tarea.save()
        tarea_editada = Tarea.objects.get(pk=self.tarea.pk)
        
        self.assertEqual(tarea_editada.titulo, 'Tarea editada')
        self.assertEqual(tarea_editada.email, 'edited@example.com')
        self.assertEqual(tarea_editada.descripcion, 'Esta es una tarea editada')

    def test_eliminar_tarea(self):
        """Delete tarea"""
        self.tarea.delete()
        tarea_eliminada = Tarea.objects.filter(pk=self.tarea.pk).first()
        self.assertIsNone(tarea_eliminada)

    def test_str_metodo_tarea(self):
        """String tarea method test"""
        self.assertEqual(str(self.tarea), 'Tarea de prueba')
