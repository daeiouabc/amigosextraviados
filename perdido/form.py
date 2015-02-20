from django.forms import ModelForm, TextInput, Textarea, ChoiceField, Select, DateField
from .models import Perdido


class PerdidoForm(ModelForm):
    class Meta:
        model = Perdido
        fields = ['nombre', 'especie', 'raza', 'sexo', 'descripcion', 'position', 'photo', 'fechaDesaparicion', 'dirDesaparicion']
        SEXO_CHOICES = ((0, ""), (1, "Macho"), (2, "Hembra"))
        widgets = {
            'raza': TextInput(),
            'sexo': Select(choices=SEXO_CHOICES),
        }

    class Media:
        js = ('js/forms/formMascota.js', )
        css = {
            'all': ('layout.css',)
        }
