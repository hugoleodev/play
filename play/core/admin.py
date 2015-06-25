from django.contrib import admin
from play.core.models import Filme


class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sinopse', 'image_tag', 'created_at')

admin.site.register(Filme, FilmeAdmin)
