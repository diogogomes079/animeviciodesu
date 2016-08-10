# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listar_animes, name='listar_animes'),

]
