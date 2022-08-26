from django.contrib import admin
from django.urls import path
from movie import views
urlpatterns = [
    path('getmovies/',views.getMovieDetails),
]
print('--------hu jagdish')