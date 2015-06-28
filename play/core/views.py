from play.core.models import Filme
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class FilmeList(ListView):
    model = Filme


class FilmeDetail(DetailView):
    model = Filme

    def get_object(self):
        filme = get_object_or_404(Filme, slug=self.kwargs['slug'])
        return filme
