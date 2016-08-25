# coding=utf-8

from .models import Genero


def generos(request):
    return {
        'generos' : Genero.objects.all()
    }
