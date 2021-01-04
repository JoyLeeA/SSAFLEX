from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, GenreSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


@api_view(['GET'])
def movies(request):
    movie_list = Movie.objects.all()
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genres(request):
    genre_list = Genre.objects.all()
    serializer = GenreSerializer(genre_list, many=True)
    return Response(serializer.data)

