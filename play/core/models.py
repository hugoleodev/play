from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from django.db.models.query import QuerySet


class FilmeQuerySet(QuerySet):
    def filmes_relacionados(self, filme_id, generos, atores):
        return self.raw("""
        SELECT f.*, count(distinct fg.genero_id) count_generos,
        count(distinct fa.ator_id) count_ator
        FROM core_filme f, core_filme_generos fg, core_filme_atores fa
        where fa.filme_id = f.id
        and fg.filme_id = f.id
        and fa.ator_id in (%s)
        and fg.genero_id in (%s)
        and f.id != '%s'
        group by f.id
        order by count_generos desc, count_ator desc
            """ % (",".join(generos), ",".join(atores), filme_id))


class FilmeManager(models.Manager):

    def get_queryset(self):
        return FilmeQuerySet(self.model, using=self._db)

    def filmes_relacionados(self, filme):
        if not isinstance(filme, Filme):
            raise ValueError("The filme argument must be a Filme instance")

        generos = map(lambda genero: str(genero.id), filme.generos.all()) or []
        atores = map(lambda ator: str(ator.id), filme.atores.all()) or []
        return self.get_queryset().filmes_relacionados(filme.id, generos, atores)


class Filme(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sinopse = models.TextField(max_length=11)
    capa = ResizedImageField(upload_to='filmes/', size=[220, 283])
    generos = models.ManyToManyField('Genero')
    atores = models.ManyToManyField('Ator')
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="criado em")

    objects = FilmeManager()

    def image_tag(self):
        return u'<img src="%s%s" width="168" heigth="216" />' % (settings.MEDIA_URL, self.capa)

    image_tag.short_description = 'Capa'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Filme, self).save(*args, **kwargs)


class Genero(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return "/generos/%s/" % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Genero, self).save(*args, **kwargs)


class Ator(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    pais = models.CharField(max_length=20)
    foto = ResizedImageField(upload_to='atores/', size=[160, 100])
    slug = models.SlugField()

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return "/atores/%d/" % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Ator, self).save(*args, **kwargs)
