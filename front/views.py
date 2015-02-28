from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))


from perdido.form import PerdidoForm


def perdidos(request):
    form = PerdidoForm()
    return render_to_response('perdidos.html', {'form': form}, context_instance=RequestContext(request))


def encontrados(request):
    return render_to_response('encontrados.html', context_instance=RequestContext(request))

from adopcion.form import AdopcionForm


def adopciones(request):
    form = AdopcionForm()
    return render_to_response('adopciones.html', {'form': form}, context_instance=RequestContext(request))


def Detallemascota(request):
    return render_to_response('Detallemascota.html', context_instance=RequestContext(request))


class Offline(TemplateView):
    template_name = "offline.html"

from perdido.models import Perdido
from django.http import Http404


def perdido_detail(request, mascota_id):
    try:
        mascota = Perdido.objects.get(pk=mascota_id)
        return render_to_response('detallePerdido.html', {'mascota': mascota}, context_instance=RequestContext(request))
    except Perdido.DoesNotExist:
        raise Http404

from adopcion.models import Adopcion


def adopcion_detail(request, mascota_id):
    try:
        mascota = Adopcion.objects.get(pk=mascota_id)
        return render_to_response('detalleAdopcion.html', {'mascota': mascota}, context_instance=RequestContext(request))
    except Adopcion.DoesNotExist:
        raise Http404
