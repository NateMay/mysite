from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from movies.forms import GenreForm
from movies.models import Genre, Movie



class MovieList(LoginRequiredMixin, View):
    def get(self, req):

        return render(req, 'movies/movie_list.html', {
            'count': Genre.objects.all().count(),
            'movie_list': Movie.objects.all()
        })

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:movie_list')

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:movie_list')

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    template = 'movie/movie_confirm_delete.html'
    success_url = reverse_lazy('movies:movie_list')



class GenreView(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, 'movies/genre_list.html', {
            'genre_list': Genre.objects.all()
        })

class GenreCreate(LoginRequiredMixin, View):
    template = 'movies/genre_form.html'
    success_url = reverse_lazy('movies:movie_list')

    def get(self, request):
        return render(request, self.template, {'form': GenreForm() })

    def post(self, request):
        form = GenreForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class GenreUpdate(LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:genre_list')

class GenreDelete(LoginRequiredMixin, DeleteView):
    model = Genre
    template = 'movie/genre_confirm_delete.html'
    success_url = reverse_lazy('movies:genre_list')
