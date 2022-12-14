from datetime import datetime, timezone
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    cumpleaños = models.DateField()
    horario = models.IntegerField()
    legajo = models.IntegerField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Correo:{self.correo} - Cumpleaños:{self.cumpleaños} - Horario:{self.horario} - Legajo:{self.legajo}"

class Stock(models.Model):
    nombre = models.CharField(max_length=64)
    autor = models.CharField(max_length=64)
    genero = models.CharField(max_length=64)
    cantidad = models.IntegerField()
    pequeña_reseña = models.TextField(max_length=300)
    
    def __str__(self):
        return f"Nombre:{self.nombre} - Autor:{self.autor} - Genero:{self.genero} - Cantidad:{self.cantidad} - Pequeña_reseña:{self.pequeña_reseña} - Imagen:{self.imagen} - FechaPosteo:{self.fecha_posteo}"

class Resenia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_libro = models.CharField(max_length=64)
    puntaje = models.IntegerField()
    reseña = models.TextField(max_length=280)
    


    def __str__(self):
        return f"Usuario: {self.user} - Nombre:{self.nombre_libro} - Puntaje:{self.puntaje} - Reseña:{self.reseña}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares",null=True,blank=True)
    def __str__(self):
        return f"User:{self.user} - Imagen:{self.imagen}"

class InformacionAdicional(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion_personal= models.CharField(max_length=200,null=True,blank=True)
    pagina_web=models.URLField(max_length=200,null=True,blank=True)
    def __str__(self):
        return f"User:{self.user} - DescripcionPersonal:{self.descripcion_personal} - PaginaWeb:{self.pagina_web}"

class Imagen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_libro= models.CharField(max_length=64)
    subtitulo= models.CharField(max_length=64)
    cuerpo=RichTextField(blank=True, null=True)
    autor=models.CharField(max_length=64)
    imagen= models.ImageField(upload_to="imagenes",null=True,blank=True)
    fecha_posteo=models.DateField(auto_now_add=True)

    
    def __str__(self):
        return f"User:{self.user} - Libro:{self.nombre_libro}- Imagen:{self.imagen} #- FechaPosteo:{self.fecha_posteo}"