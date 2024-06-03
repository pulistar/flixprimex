
from django.contrib import admin
from django.urls import path, include
from api_flixprimex import urls  as pelicula_urls
from api_flixprimex import urls as series_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/peliculas/', include(pelicula_urls)),
    path('api/series/', include(series_urls))
    
    
]
