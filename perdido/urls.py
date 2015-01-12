from django.conf.urls import patterns, url

from . import views

from commons.routes import CustomOwnerRouter


routerPerdidoRUD = CustomOwnerRouter()
routerPerdidoRUD.register(r'edit', views.PerdidoViewSet)


routerPerdidoCreate = patterns('', url(r'', views.CreatePerdido.as_view({'post': 'create'})), )
