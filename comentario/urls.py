from django.conf.urls import patterns, url
from commons.routes import CustomOwnerRouter

from . import views


#rutas para Leer, Actualizar y Eliminar
routerComentarioRUD = CustomOwnerRouter()
routerComentarioRUD.register(r'edit', views.ComentarioViewSet)

routerComentario = patterns(
    '',
    #crear
    url(r'^create', views.CrearComentario.as_view({'post': 'create'})),

    #listar comentarios de una publicacion
    url(r'^list/(?P<pk>\d+)', views.ComentarioLista.as_view()), )


routerComentario += routerComentarioRUD.urls
