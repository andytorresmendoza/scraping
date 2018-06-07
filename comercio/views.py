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
       #'HTML' : strip_tags(textohtml)
     'HTML' : strip_tags([i for i in zip(listap, frecuenciaPalab)])
    # 'URL' : c
    }
    return JsonResponse(data)

strip = strip_tags(textohtml) 
listap = strip.split() 

frecuenciaPalab = []
for w in listap:
    frecuenciaPalab.append(listap.count(w))


