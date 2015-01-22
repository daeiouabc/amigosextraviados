from django.conf.urls import patterns, url

from . import views

routerNotificacion = patterns(
    '',
    url(r'^all', views.NotificacionLista.as_view()),
    url(r'^unread', views.NotificacionUnRead.as_view()), )
