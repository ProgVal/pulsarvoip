from django.conf.urls import patterns, include, url
from django.contrib import admin
from pulsarvpn.views import *

urlpatterns = patterns(
    '',
    url(r'^welcomepage/$', welcome, name='welcome'),
    url(r'^step1/$', step1, name='step1'),
    url(r'^step2/$', generate_keys, name='step2'),




)    