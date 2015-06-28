# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from play.core.views import FilmeList, FilmeDetail


urlpatterns = patterns('play.core.views',

    url(r'^filmes/(?P<slug>[-_\w]+)/$',
        FilmeDetail.as_view(),
        name='film-detail'),

    url(r'^$', FilmeList.as_view(), name='home'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
