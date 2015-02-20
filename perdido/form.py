from django.forms import ModelForm, TextInput, Textarea, ChoiceField
from .models import Perdido


class PerdidoForm(ModelForm):
    class Meta:
        model = Perdido
        fields = ['nombre', 'especie', 'raza', 'sexo', 'descripcion', 'position', 'foto', 'FechaDesaparicion', 'DirDesaparicion']
        CHOICES = (("1", "Macho"), ("2", "Hembra"))
        widgets = {
            'nombre': TextInput(attrs={}),
            'especie': TextInput(attrs={}),
            'raza': TextInput(attrs={}),
            'sexo': ChoiceField(choices=CHOICES, attrs={}),
            'descripcion': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
