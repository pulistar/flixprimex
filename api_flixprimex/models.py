from django.db import models


class peliculas(models.Model):
    url = models.CharField(max_length=500, null= True)
    titulo = models.CharField( max_length=100)
    sinopsis = models.CharField(max_length=100)
    genero= models.CharField( max_length=100)
    director = models.CharField(max_length=100)
    actores = models.CharField(max_length=100)
    fecha_estreno =models.DateField()
    duracion = models.DecimalField(max_digits=5, decimal_places=2)
    



class series(models.Model):
    url = models.CharField(max_length=500, null= True)
    titulo = models.CharField( max_length=100)
    sinopsis = models.CharField(max_length=100)
    genero= models.CharField( max_length=100)
    director = models.CharField(max_length=100)
    actores = models.CharField(max_length=100)
    fecha_estreno =models.DateField()
    temporada = models.IntegerField()
    duracion = models.DecimalField(max_digits=5, decimal_places=2)
    





