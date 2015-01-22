from django.conf.urls import patterns, url

from . import views

routerNotificacion = patterns(
    '',
    url(r'^all', views.NotificationLista.as_view()),
    url(r'^unread', views.NotificationUnRead.as_view()), )
