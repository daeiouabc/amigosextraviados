from django.conf.urls import patterns, url
from commons.routes import CustomOwnerRouter

from . import views


#rutas para Leer, Actualizar y Eliminar
routerUsuarioRUD = CustomOwnerRouter()
routerUsuarioRUD.register(r'edit', views.UsuarioViewSet)

routerUsuario = patterns('',
    #crear
    url(r'^create', views.CrearUsuario.as_view({'post': 'create'})),
    #publico
    url(r'^(?P<pk>\d+)', views.UsuarioPublico.as_view(), name='usuario-pub'), )

#Leer, Actualizar y Eliminar
routerUsuario += routerUsuarioRUD.urls
