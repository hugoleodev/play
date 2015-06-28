from django.test import TestCase
from django.core.urlresolvers import reverse as r
from model_mommy import mommy
from play.core.models import Filme


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
        filme.save()

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
