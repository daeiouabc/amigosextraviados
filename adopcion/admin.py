from django.contrib import admin
from .models import Adopcion


class AdopcionAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaPublicacion', )

admin.site.register(Adopcion, AdopcionAdmin)
