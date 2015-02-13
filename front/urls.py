from django.conf.urls import patterns, url

urlpatterns = patterns('',

  url(r'^$', 'front.views.index', name='index'),
  url(r'^perdidos/$', 'front.views.perdidos', name='perdidos'),
  url(r'^encontrados/$', 'front.views.encontrados', name='encontrados'),
  url(r'^adopciones/$', 'front.views.adopcion', name='adopciones'),
  url(r'^perdidos/(?P<mascota_id>\d+)/$', 'front.views.detail', name='detail'),
  url(r'^encontrados/(?P<mascota_id>\d+)/$', 'front.views.detail', name='detail'),
  url(r'^adopciones/(?P<mascota_id>\d+)/$', 'front.views.detail', name='detail'),
  )
