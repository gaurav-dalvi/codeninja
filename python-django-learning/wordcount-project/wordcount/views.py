from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'foo': 'This is from templates'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    wordcount = {}
    for word in wordlist:
        if word in wordcount.keys():
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'freq': sortedwords})