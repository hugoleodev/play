# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from model_mommy import mommy
from play.core.models import Filme, Genero, Ator


class HomepageTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_get(self):
        'GET / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Homepage must use template core/filme_list.html'
        self.assertTemplateUsed(self.resp, "core/filme_list.html")


class FilmeDetailTest(TestCase):

    def setUp(self):
        filme = mommy.make(Filme,
                           nome="As Bem Armadas",
                           sinopse="A agente especial do FBI Sarah Ashburn")

        genero = mommy.make(Genero, nome="Comédia")

        ator = mommy.make(Ator,
                          nome="Scarlett Johansson",
                          pais="Estados Unidos")

        filme.generos.add(genero)
        filme.atores.add(ator)

        self.resp = self.client.get(r('core:film-detail',
                                    kwargs={'slug': 'as-bem-armadas'}))

    def test_get(self):
        'GET should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'FilmeDetail must use template core/filme_detail.html'
        self.assertTemplateUsed(self.resp, "core/filme_detail.html")

    def test_context_with_filme(self):
        'Context must have a Filme instance'
        filme = self.resp.context['filme']
        self.assertIsInstance(filme, Filme)

    def test_html(self):
        'HTML must contain data'
        self.assertContains(self.resp, 'As Bem Armadas')
        self.assertContains(self.resp, 'A agente especial do FBI Sarah Ashburn')
        self.assertContains(self.resp, '/generos/comedia/')
        self.assertContains(self.resp, '/atores/scarlett-johansson/')


class GeneroDetailTest(TestCase):

    def setUp(self):
        genero = mommy.make(Genero, nome="Comédia")
        genero.save()

        self.resp = self.client.get(r('core:genero-detail',
                                    kwargs={'slug': 'comedia'}))

    def test_get(self):
        'GET should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'GeneroDetail must use template core/genero_detail.html'
        self.assertTemplateUsed(self.resp, "core/genero_detail.html")

    def test_context_with_filme(self):
        'Context must have a Genero instance'
        genero = self.resp.context['genero']
        self.assertIsInstance(genero, Genero)

    def test_html(self):
        'HTML must contain data'
        self.assertContains(self.resp, 'Comédia')


class AtorDetailTest(TestCase):

    def setUp(self):
        ator = mommy.make(Ator,
                          nome="Scarlett Johansson",
                          pais="Estados Unidos")
        ator.save()

        self.resp = self.client.get(r('core:ator-detail',
                                    kwargs={'slug': 'scarlett-johansson'}))

    def test_get(self):
        'GET should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'AtorDetail must use template core/ator_detail.html'
        self.assertTemplateUsed(self.resp, "core/ator_detail.html")

    def test_context_with_filme(self):
        'Context must have a Ator instance'
        ator = self.resp.context['ator']
        self.assertIsInstance(ator, Ator)

    def test_html(self):
        'HTML must contain data'
        self.assertContains(self.resp, 'Scarlett Johansson')
