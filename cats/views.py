from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.forms import BreedForm
from cats.models import Breed, Cat


class CatList(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, 'cats/cat_list.html', {
            'count': Breed.objects.all().count(),
            'cat_list': Cat.objects.all()
        })

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    template = 'cats/cat_confirm_delete.html'
    success_url = reverse_lazy('cats:cat_list')



class BreedView(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, 'cats/breed_list.html', {
            'breed_list': Breed.objects.all()
        })

class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cat_list')

    def get(self, request):
        return render(request, self.template, {'form': BreedForm() })

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    template = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('cats:breed_list')
