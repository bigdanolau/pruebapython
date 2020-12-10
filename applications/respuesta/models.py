from django.db import models
from applications.pregunta.models import Pregunta
# Create your models here.

# Create your models here.

class Respuesta(models.Model):

    titulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=100, blank=False)
    publicado = models.BooleanField(default=True)
    pregunta  = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)
    
    