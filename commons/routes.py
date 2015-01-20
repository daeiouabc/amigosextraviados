from rest_framework.routers import Route, SimpleRouter, DefaultRouter


class CustomOwnerRouter(SimpleRouter):
    """
    Rutas para, obtener, actualizar y destruir.
    Se omite listar y crear
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

"""
class MascotasCercaRouter(DefaultRouter):
        routes = [
        Route(
            url=r'^{prefix}/((?P<pk>\d+)/)?info$',
            mapping={'get': 'info'},
            name='{basename}-info',
            initkwargs={}
        )
    ] + DefaultRouter.routes
"""
