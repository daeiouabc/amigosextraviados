# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import Adopcion


class AdopcionForm(ModelForm):
    """docstring for AdopcionForm"""
    class Meta():
        model = Adopcion
        fields = ['nombre', 'especie', 'raza', 'sexo', 'descripcion', 'position', 'photo', 'dirContacto']

        SEXO_CHOICES = (('0', ''), ('1', 'Macho'), ('2', "Hembra"))
        attrs = {"class": "form-control"}
        widgets = {
            'nombre': TextInput(attrs),
            'especie': TextInput(attrs),
            'raza': TextInput(attrs),
            'descripcion': Textarea(attrs),
            'dirContacto': DateInput(attrs),
            'sexo': TextInput(attrs),
        }

        widgets['nombre'].attrs['placeholder'] = "¿Cómo se llama?"
        widgets['especie'].attrs['placeholder'] = "¿Es un perro, gato o tortuga?"
        widgets['raza'].attrs['placeholder'] = "¿Sabes su raza?, un buen amo debería saberla"
        widgets['descripcion'].attrs['placeholder'] = "Cuéntanos su historia"
        widgets['sexo'].attrs['placeholder'] = "Ese checkbox para el sexo es una #$%"
        widgets['dirContacto'].attrs['placeholder'] = "¿En donde se encuentra?"

        widgets['descripcion'].attrs['rows'] = 9
        widgets['descripcion'].attrs['cols'] = 2

    class Media:
        js = ('js/forms/formMascota.js', )
        css = {
            #'all': ('layout.css',)
        }