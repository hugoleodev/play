from play.core.models import Filme
from django.views.generic import ListView


class FilmeList(ListView):
    model = Filme
