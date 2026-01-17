# I have created this file -- aditya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, 'index.html')

   #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #check which checkbox is on
    if removepunc == 'on':
       #analyzed = djtext
       punctuations = '''.,?!:;"'()[]{}-—_/\@#$%&*+=<>|~`…...‘’“”'''
       analyzed = ""
       for char in djtext:
          if char not in punctuations:
            analyzed = analyzed+char

       params = {'purpose':'Removed punctuation', 'analyzed_text': analyzed}
       djtext = analyzed
       #return render(request, 'analyze.html', params)

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]== " " :
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}

    if (removepunc != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and fullcaps != 'on'):
        return HttpResponse("Error! Please select any operation.")

    return render(request, 'analyze.html', params)

def about(request):
        return render(request, 'about.html')

def contact(request):
        return render(request, 'contact.html')

