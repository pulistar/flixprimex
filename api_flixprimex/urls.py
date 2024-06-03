from django.urls import path
from .views import peliculas_api_view, series_api_view


urlpatterns = [
    path('listar-peliculas/<int:pkid>', peliculas_api_view.as_view(), name='listar-peliculas'),
    path('listar-peliculas', peliculas_api_view.as_view(), name='listar-todas-las-peliculas'),
    path('crear-pelicula', peliculas_api_view.as_view(), name='crear-pelicula'),
    path('actualizar-pelicula/<int:pkid>', peliculas_api_view.as_view(), name='actualizar-pelicula'),
    path('eliminar-pelicula/<int:pkid>', peliculas_api_view.as_view(), name='eliminar-pelicula'),
    path('listar-series/<int:pkid>', series_api_view.as_view(), name='listar-series'),
    path('listar-series', series_api_view.as_view(), name='listar-todas-las-series'),
    path('crear-serie', series_api_view.as_view(), name='crear-serie'),
    path('actualizar-serie/<int:pkid>', series_api_view.as_view(), name='actualizar-serie'),
    path('eliminar-serie/<int:pkid>', series_api_view.as_view(), name='eliminar-serie'),
]


