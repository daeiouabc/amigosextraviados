import django_filters
from .models import Perdido


class PerdidoFilter(django_filters.FilterSet):
    class Meta:
        model = Perdido
        fields = ('especie', 'raza', )
