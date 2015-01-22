from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from notifications.models import Notification

from .serializers import NotificationSerializer


class NotificationLista(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Lista Todas las notificaciones del usuario que se encuentra autenticado
    """
    model = Notification
    queryset = {}
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        #obtiene todas las notificaciones del usuario autenticado
        instances = request.user.notifications.all()

        #serializa las notificaciones
        serializer = self.get_serializer(instances, many=True)

        #retorna el JSON
        return Response(serializer.data)


class NotificationUnRead(NotificationLista):
    """
    Lista todas las notificaciones marcadas sin leer
    """
    def list(self, request, *args, **kwargs):
        #obtiene todas las notificaciones sin leer del usuario autenticado
        instances = request.user.notifications.unread().order_by('-timestamp')

        #serializa las notificaciones
        serializer = self.get_serializer(instances, many=True)

        #retorna el JSON
        return Response(serializer.data)
