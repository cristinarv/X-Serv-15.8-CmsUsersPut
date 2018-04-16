# Cristina del Río 
from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def inicio_pag(request):
    resp = "<u><h4>La lista de las paginas es:</h4></u><br>"
    list_pags = Pages.objects.all()
    for pag in list_pags:
        resp += "<li><a href=" + str(pag.id) + ">" +  pag.name +  "</a></li><br>"
    return HttpResponse(resp)
def pag(request, id):
    try:
        pag = Pages.objects.get(id=id)
        resp = "El nombre es: " + pag.name + " <br>Su página es: " + pag.page
        return HttpResponse(resp)
    except Pages.DoesNotExist:
        return HttpResponseNotFound("<h2>La página introducida no existe</h2>")
