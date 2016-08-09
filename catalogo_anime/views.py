# coding=utf-8

from django.shortcuts import render

from .models import Anime

def listar_animes(request):
    context = {
        'animes_list' : Anime.objects.all()
    }
    return render(request, 'catalogo_anime/galeria_anime_manga.html',context)
