from django.db import models


class Filme(models.Model):
    nome = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=11)
    capa = models.ImageField(upload_to='filmes/')
