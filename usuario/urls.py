from django.conf.urls import patterns, url

from commons.routes import CustomOwnerRouter

from . import views


#rutas para Leer, Actualizar y Eliminar
routerUsuarioRUD = CustomOwnerRouter()
routerUsuarioRUD.register(r'edit', views.UsuarioViewSet)

#ruta para crear
routerUsuarioCreate = patterns('', url(r'', views.CrearUsuario.as_view({'post': 'create'})), )

#ruta publica
routerUsuarioPublico = patterns('', url(r'', views.UsuarioPublico.as_view()), )
