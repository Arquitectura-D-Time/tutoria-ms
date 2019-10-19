from django.db import models

# Create your models here.
# links=tutoria Link=Tutoria
class Tutoria(models.Model):
    materia = models.TextField(default='')
    descripcion = models.TextField(blank=True)
    cupos = models.SmallIntegerField()
    idtutor = models.SmallIntegerField()
    idtoken = models.TextField(blank=True)


