from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # texto = "<h1>Mi web personal</h1><h2>IES La Marisma</h2>"          
    # texto += "<ul><li><a href='about/'>Acerca de</a></li><li><a href='contacto/'>Contacto</a></li></ul>"
    # return HttpResponse(texto)
    return render (request,"index.html")

def about(request):
    texto = "<h1>Mi web personal</h1><h2>IES La Marisma</h2>"
    texto += "<ul><li><a href='/'>Portada</a></li></ul>"
    texto += "<h1>Acerca de</h1>"
    texto += "<p>Soy un programador</p>"
    return HttpResponse(texto)

def contacto(request):
    texto = "<h1>Mi web personal</h1><h2>IES La Marisma</h2>"
    texto += "<ul><li><a href='/'>Portada</a></li></ul>"
    texto += "<h1>Contacto</h1>"
    texto += "<ul><li><a href='mailto:user@gmail.com'>Email</a></li><li><a href='https://es-es.facebook.com/' tarjet='_blank'>Facebook</a></li></ul>"
    return HttpResponse(texto)