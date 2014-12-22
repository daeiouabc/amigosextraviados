from django.conf.urls import patterns, url
from rest_framework.routers import Route, SimpleRouter
from . import views


class CustomOwnerUsuarioRouter(SimpleRouter):
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
        ),
    ]


class CustomCreateUsuarioRouter(SimpleRouter):
    """
    Rutas para, obtener, actualizar y destruir un usuario.
    Se omite listar los usuarios
    """
    routes = [
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'post': 'create'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        ),
    ]


routerUsuarioRUD = CustomOwnerUsuarioRouter()
routerUsuarioRUD.register(r'usuario', views.Usuario)


urlCrearUsuario = patterns('',url(r'usuario', views.CrearUsuario.as_view({'post': 'create'})),)

#routerCreateUsuario = CustomCreateUsuarioRouter()
#routerCreateUsuario.register(r'usuario', views.CrearUsuario)
