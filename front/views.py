from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))


def perdidos(request):
    return render_to_response('perdidos.html', context_instance=RequestContext(request))


def encontrados(request):
    return render_to_response('encontrados.html', context_instance=RequestContext(request))


def Detallemascota(request):
    return render_to_response('Detallemascota.html', context_instance=RequestContext(request))
