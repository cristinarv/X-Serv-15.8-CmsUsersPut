# Cristina del Río 
from django.shortcuts import render
from cms_users_put.models import Pages
from django.http import HttpResponse

# Create your views here.
FORMULARIO= """
<form action="" method="POST">
    <input type='text' name='name'><br>
    <input type="text" name="page"/>
    <input type="submit" value="Enviar"/>
</form>"""

def inicio_pag(request):
    if request.user.is_authenticated():
        resp = "Logged in as " + request.user.username
        resp += ". <a href='/logout'>Logout</a><br>"
    else:
        resp = "Not logged in. <a href='/login'>Login</a><br>"
    resp += "<u><h4>La lista de las paginas es:</h4></u>"
    list_pags = Pages.objects.all()
    for pag in list_pags:
        resp +=  "<ul><li>" + pag.name + " ==> " + pag.page + "</ul></li>"
    return HttpResponse(resp)
