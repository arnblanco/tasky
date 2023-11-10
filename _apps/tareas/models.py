"""Tareas models"""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from _tasks.send_email import send_mail

# pylint: disable=no-member
class Tarea(models.Model):
	"""Tareas Model"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	titulo = models.CharField(max_length=128, null=False, blank=False)
	email = models.EmailField(max_length=128, null=False, blank=False)
	descripcion = models.TextField(null=False, blank=False)
	fecha_vencimiento = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = models.Manager()
	
	def __str__(self):
		return f"{0}".format(self.titulo)
		
		
@receiver(post_save, sender=Tarea)
def send_email_notification(sender, instance, created, **kwargs):
	"""Tareas receiver"""
	if created:
		send_mail(
			[instance.email,],
			'Nueva Tarea',
			'mailing/nueva-tarea.html',
			{'data': instance}
		)
