from play.core.models import Filme, Genero, Ator
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class FilmeList(ListView):
    model = Filme


class FilmeDetail(DetailView):
    model = Filme

    def get_object(self):
        filme = get_object_or_404(Filme, slug=self.kwargs['slug'])
        return filme


class GeneroDetail(DetailView):
    model = Genero

    def get_object(self):
        genero = get_object_or_404(Genero, slug=self.kwargs['slug'])
        return genero


class AtorDetail(DetailView):
    model = Ator

    def get_object(self):
        ator = get_object_or_404(Ator, slug=self.kwargs['slug'])
        return ator
