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
#t = ''
#Buscar
#for  url in soup.find_all('a'):

 #  c += '[' + url.get('href')+']' 
textohtml = soup.prettify()


def getcomercio(request):
    data={
      'Titulo' : soup.title.string,
       'HTML' : strip_tags(textohtml)
    #   'URL' : c
    }
    return JsonResponse(data)

strip = strip_tags(textohtml) 
listap = strip.split()
#mensaje9 = listap
#mensaje9a = mensaje9[1:5000]
#print(listap)  
frecuenciaPalab = []
for w in listap:
    frecuenciaPalab.append(listap.count(w))

#print("Cadena\n" + cadenaPalabras +"\n")
#print("Lista\n" + str(listap) + "\n")
#print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
#print("Pares\n" + str(zip(listap, frecuenciaPalab)))
print([i for i in zip(listap, frecuenciaPalab)])

#print(d['Community'])
