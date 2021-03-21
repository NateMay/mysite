from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.forms import MakeForm
from autos.models import Make, Auto



class MainView(LoginRequiredMixin, View):
    def get(self, req):

        return render(req, 'autos/auto_list.html', {
            'count': Make.objects.all().count(),
            'auto_list': Auto.objects.all()
        })

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    template = 'auto/auto_confirm_delete.html'
    success_url = reverse_lazy('autos:auto_list')



class MakeView(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, 'autos/make_list.html', {
            'make_list': Make.objects.all()
        })

class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:auto_list')

    def get(self, request):
        return render(request, self.template, {'form': MakeForm() })

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    template = 'auto/make_confirm_delete.html'
    success_url = reverse_lazy('autos:make_list')
