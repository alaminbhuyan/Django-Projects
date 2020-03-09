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

def analyze(request):
    djtext = (request.GET.get('text', 'default'))
    removepunc = (request.GET.get('removepunc', 'off'))
    print(removepunc)
    print(djtext)
    #analyzed = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char  not in punctuations:
                analyzed = analyzed+char
        text = {'purpose':'Remove punctations','analyzed_text':analyzed}
        return render(request,'analyze.html',text)
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
