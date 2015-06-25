# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('play.core.views',

    url(r'^$', 'home', name='home'),
)
