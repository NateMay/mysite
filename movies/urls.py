from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [

    path('', views.MovieList.as_view(), name='movie_list'),
    path('main/create', views.MovieCreate.as_view(), name='movie_create'),
    path('main/<int:pk>/update', views.MovieUpdate.as_view(), name='movie_update'),
    path('main/<int:pk>/delete', views.MovieDelete.as_view(), name='movie_delete'),

    path('lookup', views.GenreView.as_view(), name='genre_list'),
    path('lookup/create', views.GenreCreate.as_view(), name='genre_create'),
    path('lookup/<int:pk>/update', views.GenreUpdate.as_view(), name='genre_update'),
    path('lookup/<int:pk>/delete', views.GenreDelete.as_view(), name='genre_delete')
]