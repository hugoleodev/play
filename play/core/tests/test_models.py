from django.test import TestCase
from django.core.files import File
from django.conf import settings
from datetime import datetime
from unipath import Path
from play.core.models import Filme


class FilmeTest(TestCase):
    def setUp(self):
        self.file_stub = settings.PROJECT_DIR.child('core',
                                                    'tests',
                                                    'stubs',
                                                    'cartaz1.jpg')

        self.obj = Filme(
            nome="As Bem Armadas",
            sinopse="A agente especial do FBI Sarah Ashburn",
            capa=File(open(self.file_stub))
        )

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

    def tearDown(self):
        filmes = Filme.objects.all()
        map(lambda filme: Path(filme.capa.path).remove(), filmes)
