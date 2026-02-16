from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    numero = models.IntegerField()
    anio_publicacion = models.IntegerField()
    editorial = models.CharField(max_length=100)

    # Nuevo campo agregado para la actividad
    isbn = models.CharField(max_length=13, null=True, blank=True)
    # Campo agregado solo para demostrar migración pendiente
    fuente = models.CharField(max_length=80, null=True, blank=True)


    def __str__(self):
        return f"Papelucho #{self.numero} - {self.titulo}"
