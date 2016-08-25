# coding=utf-8

from django.contrib import admin

from .models import Anime, Genero


class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'genre', 'season', 'start_date', 'final_date', 'created', 'modified']
    search_fields = ['name , slug', 'genre__name']
    list_filter = ['created', 'modified']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name , slug']
    list_filter = ['created', 'modified']


# ou -> admin.site.register([Animes, Genero])
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Anime, AnimeAdmin)
