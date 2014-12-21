from rest_framework.routers import DefaultRouter

from . import views

routerUsuarioCRUD = DefaultRouter()
routerUsuarioCRUD.register(r'usuario', views.Usuario)
