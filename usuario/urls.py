from django.conf.urls import patterns, url
from rest_framework.routers import Route, SimpleRouter

from . import views


class CustomOwnerRouter(SimpleRouter):
    """
    Rutas para, obtener, actualizar y destruir un usuario.
    Se omite listar los usuarios
    """
    routes = [
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        )
    ]

#rutas para Leer, Actualizar y Eliminar
routerUsuarioRUD = CustomOwnerRouter()
routerUsuarioRUD.register(r'edit', views.UsuarioViewSet)

#ruta para crear
routerUsuarioCreate = patterns('', url(r'', views.CrearUsuario.as_view({'post': 'create'})), )

#ruta publica
routerUsuarioPublico = patterns('', url(r'', views.UsuarioPublico.as_view()), )
