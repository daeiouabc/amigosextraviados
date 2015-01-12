from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaPublicacion',)

admin.site.register(Comentario, ComentarioAdmin)
