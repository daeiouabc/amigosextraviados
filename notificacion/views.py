from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification

from .serializers import NotificationSerializer


class NotificationLista(ListAPIView):
    """
    Lista Todas las notificaciones del usuario que se encuentra autenticado
    """
    model = Notification
    queryset = {}
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )
    paginate_by = 10

    def get_queryset(self):
        #obtiene todas las notificaciones del usuario autenticado
        return self.request.user.notifications.all()


class NotificationUnRead(NotificationLista):
    """
    Lista todas las notificaciones marcadas sin leer
    """
    paginate_by = 5

    def get_queryset(self):
        #obtiene todas las notificaciones del usuario autenticado
        return self.request.user.notifications.unread().order_by('-timestamp')
