# coding=utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse
from model_mommy import mommy

from catalogo_anime.models import Anime, Genero

class GeneroTestCase(TestCase):

    def setUp(self):
        self.genero = mommy.make('catalogo_anime.Genero')

    def test_get_absolute_url(self):
        self.assertEquals(self.genero.get_absolute_url(),
        reverse('catalogo_anime:listar_generos', kwargs={'slug': self.genero.slug})

        )

class AnimeTestCase(TestCase):

    def setUp(self):
        self.anime = mommy.make('catalogo_anime.Anime', slug='anime')

    def test_get_absolute_url(self):
        self.assertEquals(self.anime.get_absolute_url(),
        reverse('catalogo_anime:info_anime', kwargs={'slug': 'anime'})

        )
