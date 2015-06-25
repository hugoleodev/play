# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static


urlpatterns = patterns('play.core.views',

    url(r'^$', 'home', name='home'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
