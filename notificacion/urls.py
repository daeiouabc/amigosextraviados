from rest_framework.routers import DefaultRouter

from . import views

#listar notificaciones
router = DefaultRouter()
router.register(r'^unread', views.NotificationUnRead)
router.register(r'^all', views.NotificationLista)

routerNotificacion = router.urls
