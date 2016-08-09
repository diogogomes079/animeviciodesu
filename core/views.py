# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return render(request,'index.html')

def contato (request):
    return render(request,'contato.html')

def sobre (request):
    return render(request,'sobre.html')

def anime_info (request):
    return render(request,'info_anime_manga.html')
