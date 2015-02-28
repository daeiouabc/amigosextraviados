from django.conf.urls import patterns, include, url
from django.contrib import admin

from usuario.urls import routerUsuario

from perdido.urls import routerPerdido

from adopcion.urls import routerAdopcion

from comentario.urls import routerComentario

from notificacion.urls import routerNotificacion
import notifications

from autenticacion.urls import routerToken

from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amigosExtraviados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/user/', include(routerUsuario)),
    url(r'^api/perdido/', include(routerPerdido)),
    url(r'^api/adopcion/', include(routerAdopcion)),

    url(r'^api/comment/', include(routerComentario)),
    url(r'^api/inbox/notification/', include(routerNotificacion)),

    url(r'^api/auth/', include(routerToken)),

    url(r'^', include('front.urls', namespace='front')),

    #urls temporales para el login y el logout
    #url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^inbox/notifications/', include(notifications.urls)),

    #ruta para los estaticos
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


)


from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
