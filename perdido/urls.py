from django.conf.urls import patterns, url
from rest_framework.routers import Route, SimpleRouter

from . import views


class CostomOwnerRouter(SimpleRouter):
	"""docstring for CostumOwnerRouter"""
	routes = [
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        )
    ]


routerPerdidoRUD = CostomOwnerRouter()
routerPerdidoRUD.register(r'edit', views.PerdidoViewSet)


routerPerdidoCreate = patterns('', url(r'', views.CreatePerdido.as_view({'post': 'create'})), )
