# coding=utf-8

from django.db import models


class Genero(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['name']

    def __str__(self):
        return self.name
class Anime(models.Model):

    name = models.CharField('Nome', max_length=500)
    slug = models.SlugField('Identificador', max_length=500)
    sinopse = models.TextField('Sinopse',blank=True, null=True)
    start_date = models.DateTimeField('Data de Iníco',blank=True, null=True)
    final_date = models.DateTimeField('Data do Final',blank=True, null=True)
    season = models.CharField('Temporada',max_length=10,blank=True, null=True)
    status = models.CharField('Status',max_length=100,blank=True, null=True)
    episodes = models.IntegerField('Número de Episódios',blank=True, null=True)
    a_type = models.CharField('Tipo',blank=True, null=True, max_length=100)
    image = models.ImageField(upload_to="animes/images", verbose_name='Imagem',blank=True, null=True)

    genre = models.ForeignKey('catalogo_anime.Genero', verbose_name='Gênero')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        ordering = ['name']

    def __str__(self):
        return self.name
