from play.core.models import Filme, Genero, Ator
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class FilmeList(ListView):

    def get_queryset(self):
        queryset = Filme.objects.all()
        order = self.request.GET.get("order", "asc")
        if order == "desc":
            queryset = Filme.objects.order_by("-id")

        return queryset


class FilmeDetail(DetailView):
    model = Filme

    def get_object(self):
        filme = get_object_or_404(Filme, slug=self.kwargs['slug'])
        return filme

    def get_context_data(self, **kwargs):
        context = super(FilmeDetail, self).get_context_data(**kwargs)
        context['filmes_relacionados'] = Filme.objects.filmes_relacionados(self.get_object())
        return context


class GeneroDetail(DetailView):
    model = Genero

    def get_queryset(self):
        queryset = Genero.objects.all()
        order = self.request.GET.get("order", "asc")
        if order == "desc":
            queryset = self.get_object().filme_set.order_by("-id")

        return queryset

    def get_object(self):
        genero = get_object_or_404(Genero, slug=self.kwargs['slug'])
        return genero

    def get_context_data(self, **kwargs):
        order = self.request.GET.get("order", "asc")
        context = super(GeneroDetail, self).get_context_data(**kwargs)
        context['filmes'] = self.get_object().filme_set.all()

        if order == "desc":
            context['filmes'] = self.get_object().filme_set.order_by("-id")

        return context


class AtorDetail(DetailView):
    model = Ator

    def get_object(self):
        ator = get_object_or_404(Ator, slug=self.kwargs['slug'])
        return ator
