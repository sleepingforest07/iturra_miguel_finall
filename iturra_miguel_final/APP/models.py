from django.db import models

# Create your models here.

class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechaInscripcion= models.DateField()
    institucion = models.ForeignKey(Instituciones, on_delete=models.CASCADE)
    horaInscripcion = models.TimeField()
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=150)

class DatosAutor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=30)
    email = models.EmailField()
