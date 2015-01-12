from django.conf.urls import patterns, include, url
from django.contrib import admin

from usuario.urls import routerUsuarioRUD, routerUsuarioCreate, routerUsuarioPublico
from comentario.urls import routerComentarioRUD, routerComentarioCreate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amigosExtraviados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/user/create', include(routerUsuarioCreate)),
    url(r'^api/user/', include(routerUsuarioRUD.urls)),
    url(r'^api/user/(?P<pk>\d+)', include(routerUsuarioPublico)),

    url(r'^api/comment/create', include(routerComentarioCreate)),
    url(r'^api/comment/', include(routerComentarioRUD.urls)),


    #urls temporales para el login y el logout
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),


)
