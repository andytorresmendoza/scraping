from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import bs4 as bs
import urllib.request
import ngram as ngram
from django.utils.html import strip_tags

# Create your views here.
sauce = urllib.request.urlopen('http://archivo.elcomercio.pe/noticias/marina-guerra-peru-51667').read()
soup = bs.BeautifulSoup(sauce,'lxml')

textohtml= ''
strip = ''
variable = []

textohtml = soup.prettify()


def getcomercio(request):
    data={
      'Titulo' : soup.title.string,
      #'HTML' : strip_tags(listap)
      #'HTML' : variable
      'HTML' : strip_tags(listap),
      'Resultado' : (var,'Coincidencias')

    
    }
    return JsonResponse(data)

strip = strip_tags(textohtml) 
listap = strip.split()

frecuenciaPalab = []
for w in listap:
    frecuenciaPalab.append(listap.count(w))
variable = ([i for i in zip(listap, frecuenciaPalab)])

var = listap.count('almirante')

if var > 0:
     print (var,'Coincidencias')

else:
    print ("Ninguna Coincidencias")





