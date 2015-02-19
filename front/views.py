from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))


def perdidos(request):
    return render_to_response('perdidos.html', context_instance=RequestContext(request))


def encontrados(request):
    return render_to_response('encontrados.html', context_instance=RequestContext(request))


def adopciones(request):
    return render_to_response('adopciones.html', context_instance=RequestContext(request))


def Detallemascota(request):
    return render_to_response('Detallemascota.html', context_instance=RequestContext(request))
