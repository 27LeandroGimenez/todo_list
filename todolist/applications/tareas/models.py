from django.db import models

# Create your models here.

class Tareas(models.Model):
    BOOLEAN_CHOICES = ((True, 'Yes'), (False, 'No'))

    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True,  verbose_name='Descripcion')
    completed = models.BooleanField(null=True, blank=True, default=False, choices=BOOLEAN_CHOICES, verbose_name='Completada')

    class Meta:
        ordering = ['completed']

    def __str__(self):
        return self.name