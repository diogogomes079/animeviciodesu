# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listar_animes, name='listar_animes'),
    url(r'^(?P<slug>[\w_-]+)/$', views.listar_generos, name='listar_generos'),
    url(r'^anime/(?P<slug>[\w_-]+)/$', views.info_anime, name='info_anime'),
]
