from django.db import models
from django.conf import settings
from django_resized import ResizedImageField


class Filme(models.Model):
    nome = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=11)
    capa = ResizedImageField(upload_to='filmes/', size=[168, 216])
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="criado em")

    def image_tag(self):
        return u'<img src="%s%s" />' % (settings.MEDIA_URL, self.capa)

    image_tag.short_description = 'Capa'
    image_tag.allow_tags = True
