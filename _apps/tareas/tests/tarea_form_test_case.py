"""Tareas form test case"""
from django.test import TestCase
from django.urls import reverse
from _apps.tareas.forms import TareaForm
from _apps.tareas.models import Tarea


class TareaFormTestCase(TestCase):
    """Tarea form test"""

    def test_validar_formulario_tarea(self):
        """Form validator"""
        data = {
            'titulo': 'Nueva Tarea',
            'email': 'nueva@example.com',
            'descripcion': 'Descripción de la nueva tarea',
        }
        form = TareaForm(data=data)
        self.assertTrue(form.is_valid())
    
    def test_validar_formulario_tarea_invalido(self):
        """"Invalid form validator"""
        data = {
            'titulo': '',
            'email': 'correo_invalido',
            'descripcion': 'Descripción de la tarea',
        }
        form = TareaForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_editar_formulario_tarea(self):
        """"Edit Tarea form validator"""
        data = {
            'titulo': 'Tarea Original',
            'email': 'original@example.com',
            'descripcion': 'Descripción original',
        }
        form = TareaForm(data=data)
        form.save()
        tarea_id = Tarea.objects.get(titulo='Tarea Original').id
        edit_data = {
            'titulo': 'Tarea Modificada',
            'email': 'modificada@example.com',
            'descripcion': 'Descripción modificada',
        }
        response = self.client.post(reverse('editar_tarea', args=[tarea_id]), data=edit_data)
        self.assertEqual(response.status_code, 302)
        tarea_editada = Tarea.objects.get(pk=tarea_id)
        self.assertEqual(tarea_editada.titulo, 'Tarea Modificada')
        self.assertEqual(tarea_editada.email, 'modificada@example.com')
        self.assertEqual(tarea_editada.descripcion, 'Descripción modificada')
    
    def test_eliminar_formulario_tarea(self):
        """"Eliminar tarea form"""
        data = {
            'titulo': 'Tarea a Eliminar',
            'email': 'eliminar@example.com',
            'descripcion': 'Descripción de la tarea a eliminar',
        }
        form = TareaForm(data=data)
        form.save()
        tarea_id = Tarea.objects.get(titulo='Tarea a Eliminar').id

        response = self.client.post(reverse('eliminar_tarea', args=[tarea_id]))
        self.assertEqual(response.status_code, 302)
        tarea_eliminada = Tarea.objects.filter(pk=tarea_id).first()
        self.assertIsNone(tarea_eliminada)
