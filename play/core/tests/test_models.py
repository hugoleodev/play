# -*- coding:utf-8 -*-

from django.test import TestCase
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from datetime import datetime
from play.core.models import Filme, Genero
from model_mommy import mommy


class FilmeTest(TestCase):

    def setUp(self):
        self.obj = mommy.make(Filme,
                              nome="As Bem Armadas",
                              sinopse="A agente especial do FBI Sarah Ashburn")

    def test_create(self):
        'Filme must have name and sinopse'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_create_with_file(self):
        'Filme must have an capa image file'
        self.obj.save()

        file_path = self.obj.capa.path

        self.failUnless(open(file_path), 'Capa image was not found')

    def test_has_created_at(self):
        'Filme must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_has_slug_field(self):
        'Filme must have a slug field based on nome field'
        self.obj.save()
        self.assertEqual(self.obj.slug, slugify(self.obj.nome))

    def test_unicode(self):
        'Filme representation should be the nome field'
        self.obj.save()
        self.assertEqual('As Bem Armadas', self.obj.__unicode__())

    def test_nome_unique(self):
        'Filme must have a unique nome field'
        self.obj.save()

        with self.assertRaises(IntegrityError):
            mommy.make(Filme,
                       nome="As Bem Armadas",
                       sinopse="A agente especial do FBI Sarah Ashburn")


class GeneroTest(TestCase):

    def setUp(self):
        self.filme = mommy.make(Filme,
                                nome="As Bem Armadas",
                                sinopse="A agente especial do FBI Sarah Ashburn")

    def test_create(self):
        genero = mommy.make(Genero, nome="Comédia", filme=self.filme)
        self.assertEqual(1, genero.pk)

    def test_unicode(self):
        genero = mommy.make(Genero, nome="Comédia", filme=self.filme)
        # abc = unicode('Comédia')
        self.assertEqual('Comédia', genero.__unicode__())

    def test_nome_unique(self):
        'Genero must have a unique nome field'
        mommy.make(Genero, nome="Comédia", filme=self.filme)

        with self.assertRaises(IntegrityError):
            mommy.make(Genero, nome="Comédia", filme=self.filme)
