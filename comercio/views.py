from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import bs4 as bs
import urllib.request
import ngram as ngram
from django.utils.html import strip_tags

# Create your views here.
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

#c = ''
textohtml= ''
strip = ''
textohtml = soup.prettify()


def getcomercio(request):
    data={
      'Titulo' : soup.title.string,
      'HTML' : strip_tags(listap)

    }
    return JsonResponse(data)

strip = strip_tags(textohtml) 
listap = strip.split()

#print(listap)  
frecuenciaPalab = []
for w in listap:
    frecuenciaPalab.append(listap.count(w))

#print("Cadena\n" + cadenaPalabras +"\n")
#print("Lista\n" + str(listap) + "\n")
#print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
#print("Pares\n" + str(zip(listap, frecuenciaPalab)))
print([i for i in zip(listap, frecuenciaPalab)])


