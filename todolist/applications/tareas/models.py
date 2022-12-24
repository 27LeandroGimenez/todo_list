from django.db import models

# Create your models here.

class Tareas(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True,  verbose_name='Descripcion')
    completed = models.BooleanField(null=True, blank=True, verbose_name='Completada')

    def __str__(self):
        return self.name