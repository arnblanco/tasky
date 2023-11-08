from django.test import TestCase
from .forms import TareaForm
from django.urls import reverse

class TareaFormTestCase(TestCase):
    def test_validar_formulario_tarea(self):
        # Crea un diccionario de datos de prueba para el formulario
        data = {
            'titulo': 'Nueva Tarea',
            'email': 'nueva@example.com',
            'descripcion': 'Descripción de la nueva tarea',
        }
        
        # Crea una instancia del formulario y pásale los datos
        form = TareaForm(data=data)
        
        # Verifica que el formulario sea válido
        self.assertTrue(form.is_valid())
    
    def test_validar_formulario_tarea_invalido(self):
        # Crea un diccionario de datos de prueba para el formulario con datos inválidos
        data = {
            'titulo': '',  # Deja el título en blanco, lo cual es inválido
            'email': 'correo_invalido',  # Proporciona un correo electrónico inválido
            'descripcion': 'Descripción de la tarea',
        }
        
        # Crea una instancia del formulario y pásale los datos inválidos
        form = TareaForm(data=data)
        
        # Verifica que el formulario sea inválido
        self.assertFalse(form.is_valid())
    
    def test_editar_formulario_tarea(self):
        # Crea una tarea de prueba
        data = {
            'titulo': 'Tarea Original',
            'email': 'original@example.com',
            'descripcion': 'Descripción original',
        }
        form = TareaForm(data=data)
        form.save()

        # Modifica los datos en el formulario
        tarea_id = Tarea.objects.get(titulo='Tarea Original').id
        edit_data = {
            'titulo': 'Tarea Modificada',
            'email': 'modificada@example.com',
            'descripcion': 'Descripción modificada',
        }
        
        # Realiza una solicitud POST al formulario para editar la tarea
        response = self.client.post(reverse('editar_tarea', args=[tarea_id]), data=edit_data)
        
        # Verifica que la tarea se haya editado correctamente
        self.assertEqual(response.status_code, 302)  # Verifica que se redirige correctamente
        tarea_editada = Tarea.objects.get(pk=tarea_id)
        self.assertEqual(tarea_editada.titulo, 'Tarea Modificada')
        self.assertEqual(tarea_editada.email, 'modificada@example.com')
        self.assertEqual(tarea_editada.descripcion, 'Descripción modificada')
    
    def test_eliminar_formulario_tarea(self):
        # Crea una tarea de prueba
        data = {
            'titulo': 'Tarea a Eliminar',
            'email': 'eliminar@example.com',
            'descripcion': 'Descripción de la tarea a eliminar',
        }
        form = TareaForm(data=data)
        form.save()

        # Obtiene el ID de la tarea que se eliminará
        tarea_id = Tarea.objects.get(titulo='Tarea a Eliminar').id

        # Realiza una solicitud POST al formulario para eliminar la tarea
        response = self.client.post(reverse('eliminar_tarea', args=[tarea_id]))

        # Verifica que la tarea se haya eliminado correctamente
        self.assertEqual(response.status_code, 302)  # Verifica que se redirige correctamente
        tarea_eliminada = Tarea.objects.filter(pk=tarea_id).first()
        self.assertIsNone(tarea_eliminada)