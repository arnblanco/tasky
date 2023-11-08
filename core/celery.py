from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# establece la configuración predeterminada del módulo Django para 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')

# Utiliza una cadena de configuración en el objeto de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga las tareas de todos los módulos registrados en la configuración de INSTALLED_APPS
app.autodiscover_tasks()