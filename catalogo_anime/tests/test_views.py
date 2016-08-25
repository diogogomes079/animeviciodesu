# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalogo_anime.models import Anime, Genero

class Listar_AnimesTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalogo_anime:listar_animes')
        self.animes = mommy.make('catalogo_anime.Anime', _quantity=10)

    def tearDown(self):
        Anime.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'catalogo_anime/galeria_anime_manga.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('animes_list' in response.context)
        listar_animes = response.context['animes_list']
        self.assertEquals(listar_animes.count(), 10)
