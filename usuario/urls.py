from django.conf.urls import patterns, url
from commons.routes import CustomOwnerRouter

from .views import CrearUsuario, UsuarioViewSet, UsuarioPublico, Usuario


#rutas para Leer, Actualizar y Eliminar
routerUsuarioRUD = CustomOwnerRouter()
routerUsuarioRUD.register(r'edit', UsuarioViewSet)

routerUsuario = patterns(
    '',
    #me
    url(r'^$', Usuario.as_view(), name='me'),
    #crear
    url(r'^create$', CrearUsuario.as_view({'post': 'create'}), name='create'),
    #publico
    url(r'^(?P<pk>\d+)$', UsuarioPublico.as_view(), name='public'), )

#Leer, Actualizar y Eliminar
routerUsuario += routerUsuarioRUD.urls
