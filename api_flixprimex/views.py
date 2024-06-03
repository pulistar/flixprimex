from django.shortcuts import render
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from api_flixprimex.models import peliculas, series
from api_flixprimex.serializer import peliculas_serializer, series_serializer



class peliculas_api_view(APIView):
    def post(self, request,*args, **kwargs):  
        data={
            'url' : request.data.get('url'),
            'titulo': request.data.get('titulo'), 
            'sinopsis': request.data.get('sinopsis'), 
            'genero' : request.data.get('genero'), 
            'director' : request.data.get('director'),
            'actores' : request.data.get('actores'),
            'fecha_estreno' : request.data.get('fecha_estreno'),
            'duracion' : request.data.get('duracion'),
        }
        
        serializador = peliculas_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK)
        
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,*args, **kwargs): 
        lista_peliculas = peliculas.objects.all()
        serializer__peliculas= peliculas_serializer(lista_peliculas, many = True)
        return Response(serializer__peliculas.data, status=status.HTTP_200_OK)
    
    def put(self, request, pkid):
        pelicula_modificar = peliculas.objects.filter(id=pkid).update(
            url = request.data.get('url'),
            titulo = request.data.get('titulo'), 
            sinopsis = request.data.get('sinopsis'), 
            genero = request.data.get('genero'), 
            director = request.data.get('director'),
            actores = request.data.get('actores'),
            fecha_estreno = request.data.get('fecha_estreno'),
            duracion = request.data.get('duracion'),
        )

        return Response(pelicula_modificar, status=status.HTTP_200_OK)
    
    def delete(self, request, pkid): 
        pelicula_consultado = peliculas.objects.filter(id=pkid).delete()
        return Response(pelicula_consultado, status=status.HTTP_200_OK)
    



class series_api_view(APIView):
    def post(self, request,*args, **kwargs):  
        data={
            'url' :  request.data.get('url'),
            'titulo': request.data.get('titulo'), 
            'sinopsis': request.data.get('sinopsis'), 
            'genero' : request.data.get('genero'), 
            'director' : request.data.get('director'), 
            'actores' : request.data.get('actores'),
            'fecha_estreno' : request.data.get('fecha_estreno'),
            'temporada' : request.data.get('temporada'), 
            'duracion' : request.data.get('duracion'),
        }
        
        serializador = series_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK)
        
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,*args, **kwargs): 
        lista_series = series.objects.all()
        serializer__series= series_serializer(lista_series, many = True)
        return Response(serializer__series.data, status=status.HTTP_200_OK)
     

    
    def put(self, request, pkid):
        serie_modificar = series.objects.filter(id=pkid).update(
            url = request.data.get('url'),
            titulo = request.data.get('titulo'), 
            sinopsis = request.data.get('sinopsis'), 
            genero = request.data.get('genero'), 
            director = request.data.get('director'),
            actores = request.data.get('actores'),
            fecha_estreno = request.data.get('fecha_estreno'),
            temporada = request.data.get('temporada'),
            duracion = request.data.get('duracion'),
        )

        return Response(serie_modificar, status=status.HTTP_200_OK)
    
    def delete(self, request, pkid): 
        serie_consultado = series.objects.filter(id=pkid).delete()
        return Response(serie_consultado, status=status.HTTP_200_OK)



