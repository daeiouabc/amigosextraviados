from django.conf.urls import patterns, url

from .views import Index, Offline

from manifesto.views import ManifestView


urlpatterns = patterns(
    '',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^offline$', Offline.as_view(), name='offline'),
    url(r'^manifest\.appcache$', ManifestView.as_view(), name="cache_manifest"),
    url(r'^inicio/$', 'front.views.inicio', name='inicio'),
    url(r'^perdidos/$', 'front.views.perdidos', name='perdidos'),
    url(r'^perdidos/(?P<mascota_id>\d+)/$', 'front.views.perdido_detail', name='perdidos_detail'),
    url(r'^encontrados/$', 'front.views.encontrados', name='encontrados'),
    url(r'^adopciones/$', 'front.views.adopciones', name='adopciones'),
    url(r'^adopciones/(?P<mascota_id>\d+)/$', 'front.views.adopcion_detail', name='adopciones_detail'),

  #url(r'^perdidos/(?P<mascota_id>\d+)/$', 'front.views.detail', name='detail'),
  #url(r'^encontrados/(?P<mascota_id>\d+)/$', 'front.views.detail', name='detail'),
  #url(r'^adopciones/(?P<mascota_id>\d+)/$', 'front.views.detail', name='detail'),
  )
