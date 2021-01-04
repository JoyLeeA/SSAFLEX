from django.urls import path
from . import views
app_name="Movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.movies, name="movies"),
    path('genres/', views.genres, name="genres"),
]
