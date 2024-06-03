from api_flixprimex.models import peliculas, series
from rest_framework import serializers

class peliculas_serializer(serializers.ModelSerializer): 
    class Meta: 
        model= peliculas
        fields= ['id','url','titulo', 'sinopsis', 'genero', 'director','actores', 'fecha_estreno','duracion']


class series_serializer(serializers.ModelSerializer):
    class Meta:
        model = series
        fields = ['id','url','titulo', 'sinopsis', 'genero', 'director', 'actores','fecha_estreno', 'temporada', 'duracion']