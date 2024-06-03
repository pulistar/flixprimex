from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api_flixprimex.models import peliculas

class PeliculasApiViewTests(APITestCase):
    def setUp(self):
        self.pelicula_data = {
            'titulo': 'hoy se puede',
            'sinopsis': 'es una gran pelicula',
            'genero': 'accion',
            'director': 'varios',
            'actores': 'muchos',
            'fecha_estreno': '2024-01-01',
            'duracion': '120',
        }
        self.pelicula = peliculas.objects.create(**self.pelicula_data)

    def test_get_peliculas(self):
        url = reverse('listar-todas-las-peliculas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_pelicula(self):
        url = reverse('crear-pelicula')
        response = self.client.post(url, self.pelicula_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_pelicula(self):
        url = reverse('actualizar-pelicula', kwargs={'pkid': self.pelicula.id})
        response = self.client.put(url, data=self.pelicula_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pelicula(self):
        url = reverse('eliminar-pelicula', kwargs={'pkid': self.pelicula.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


