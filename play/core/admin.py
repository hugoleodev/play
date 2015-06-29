from django.contrib import admin
from play.core.models import Filme, Genero, Ator


class GeneroInline(admin.TabularInline):
    model = Genero
    extra = 1
    exclude = ('slug',)


class GeneroAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


class AtorInline(admin.TabularInline):
    model = Ator
    extra = 1
    exclude = ('slug',)


class AtorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


class FilmeAdmin(admin.ModelAdmin):
    inlines = [GeneroInline, AtorInline]
    list_display = ('nome', 'sinopse', 'image_tag', 'created_at')
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Filme, FilmeAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Ator, AtorAdmin)
