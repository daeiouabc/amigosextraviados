from django.conf.urls import patterns, url
from commons.routes import CustomOwnerRouter  #, MascotasRouter

from . import views


#rutas para Leer, Actualizar y Eliminar
routerPerdidoRUD = CustomOwnerRouter()
routerPerdidoRUD.register(r'edit', views.PerdidoViewSet)


from rest_framework.routers import DefaultRouter

#listar perdidos
router = DefaultRouter()
router.register(r'near', views.PerdidoCercanoLista)

routerPerdido = patterns('',
    #crear
    url(r'create', views.CreatePerdido.as_view({'post': 'create'})), )

routerPerdido += router.urls
