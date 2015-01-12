from django.contrib import admin
from .models import Perdido


class PerdidoAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaPublicacion', )

admin.site.register(Perdido, PerdidoAdmin)
