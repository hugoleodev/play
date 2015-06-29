from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify


class Filme(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sinopse = models.TextField(max_length=11)
    capa = ResizedImageField(upload_to='filmes/', size=[168, 216])
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="criado em")

    def image_tag(self):
        return u'<img src="%s%s" />' % (settings.MEDIA_URL, self.capa)

    image_tag.short_description = 'Capa'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Filme, self).save(*args, **kwargs)


class Genero(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    filme = models.ForeignKey('Filme')
    slug = models.SlugField()

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Genero, self).save(*args, **kwargs)


class Ator(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    pais = models.CharField(max_length=20)
    filme = models.ForeignKey('Filme')

    def __unicode__(self):
        return self.nome
