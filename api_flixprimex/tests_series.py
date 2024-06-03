from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api_flixprimex.models import series


class SeriesApiViewTests(APITestCase):
    def setUp(self):
        self.serie_data = {
            'titulo': 'rambo',
            'sinopsis': 'mala',
            'genero': 'ficcion',
            'director': 'yo',
            'actores': 'tu',
            'fecha_estreno': '2024-01-01',
            'temporada': '1',
            'duracion': '45',
        }
        self.serie = series.objects.create(**self.serie_data)

    def test_get_series(self):
        url = reverse('listar-todas-las-series')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_serie(self):
        url = reverse('crear-serie')
        response = self.client.post(url, self.serie_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_serie(self):
        url = reverse('actualizar-serie', kwargs={'pkid': self.serie.id})
        response = self.client.put(url, data=self.serie_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_serie(self):
        url = reverse('eliminar-serie', kwargs={'pkid': self.serie.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)