from django.conf.urls import patterns, url
from commons.routes import CustomOwnerRouter  #, MascotasRouter

from . import views


#rutas para Leer, Actualizar y Eliminar
routerAdopcionRUD = CustomOwnerRouter()
routerAdopcionRUD.register(r'edit', views.AdopcionViewSet)


from rest_framework.routers import DefaultRouter

#listar perdidos
router = DefaultRouter()
router.register(r'list', views.AdopcionLista)

routerAdopcion = patterns('',
    #crear
    url(r'create', views.CreateAdopcion.as_view({'post': 'create'})), )

routerAdopcion += router.urls
routerAdopcion += routerAdopcionRUD.urls
