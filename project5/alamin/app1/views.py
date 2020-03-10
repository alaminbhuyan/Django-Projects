from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''def home(request):
    return HttpResponse('<h1>hello world<br><a href="profile">Profile</a></h1>')
def profile(request):
    return HttpResponse('<h1>This is profile page<br><a href="/">Home</a></h1>')'''
# def index(request):
#     return HttpResponse("Home")



def index(request):
    #dic = {'name':'Alamin','location':'dhaka'}
    return render(request,'index.html')
# Check checkbox values
def analyze(request):
    #Get the text
    djtext = (request.POST.get('text', 'default'))
    
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps','off'))
    newlineremove = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    charcounter = (request.POST.get('charcounter','off'))
    # print(removepunc)
    # print(djtext)
    #analyzed = djtext
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char  not in punctuations:
                analyzed = analyzed+char
        text = {'purpose':'Remove punctations','analyzed_text':analyzed}
        return render(request,'analyze.html',text)

    elif fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        text={'purpose': 'Full Capitalyzed','analyzed_text': analyzed}
        return render(request, 'analyze.html', text)
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        text={'purpose': 'Extra space remover','analyzed_text': analyzed}
        return render(request, 'analyze.html', text)
    elif newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed=analyzed+char
        text = {'purpose': 'Newline remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', text)
    elif charcounter == "on":
        analyzed= 0
        for char in djtext:
            if char == " ":
                continue
            else:
                analyzed = analyzed+1
        text = {'purpose': 'Total character', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', text)
    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")
