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

routerUsuarioCRUD = CustomOwnerUsuarioRouter()
routerUsuarioCRUD.register(r'usuario', views.Usuario)
