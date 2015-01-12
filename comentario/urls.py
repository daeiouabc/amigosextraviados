from django.conf.urls import patterns, url
from commons.routes import CustomOwnerRouter

from . import views


#ruta para crear
routerComentarioCreate = patterns('', url(r'', views.CrearComentario.as_view({'post': 'create'})), )


#rutas para Leer, Actualizar y Eliminar
routerComentarioRUD = CustomOwnerRouter()
routerComentarioRUD.register(r'edit', views.ComentarioViewSet)
