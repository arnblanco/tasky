from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tarea(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	titulo = models.CharField(max_length=128, null=False, blank=False)
	email = models.EmailField(max_length=128, null=False, blank=False)
	descripcion = models.TextField(null=False, blank=False)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % self.titulo