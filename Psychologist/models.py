from django.db import models
from django.db import models

class Psicologo(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    descripcion = models.TextField()
    experiencia = models.IntegerField(help_text="Años de experiencia")
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion_consultorio = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='psicologos/images', null=True, blank=True)

    def __str__(self):
        return self.nombre
