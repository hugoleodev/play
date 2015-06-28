from django.contrib import admin
from play.core.models import Filme, Genero


class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sinopse', 'image_tag', 'created_at')
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Filme, FilmeAdmin)
admin.site.register(Genero)
