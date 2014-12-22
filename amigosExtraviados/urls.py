from django.conf.urls import patterns, include, url
from django.contrib import admin

from usuario.urls import routerUsuarioRUD, routerUsuarioCreate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amigosExtraviados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/user/create', include(routerUsuarioCreate)),
    url(r'^api/user/', include(routerUsuarioRUD.urls)),


    #urls temporales para el login y el logout
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),


)
