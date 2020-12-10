from django.db import models

# Create your models here.

class Pregunta(models.Model):

    titulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=100, blank=False)
    publicado = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.titulo)
    