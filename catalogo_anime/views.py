# coding=utf-8

from django.shortcuts import render

from .models import Anime, Genero

def listar_animes(request):
    context = {
        'animes_list' : Anime.objects.all()
    }
    return render(request, 'catalogo_anime/galeria_anime_manga.html',context)

def listar_generos(request,slug):
    genero = Genero.objects.get(slug=slug)
    context = {
        'current_genero' : genero,
        'animes_list' : Anime.objects.filter(genre=genero),
    }
    return render(request,'catalogo_anime/galeria_genero.html',context)

def info_anime(request, slug):
    anime = Anime.objects.get(slug=slug)
    context = {
        'info_anime':anime,
    }
    return render(request,'catalogo_anime/info_anime_manga.html',context)
