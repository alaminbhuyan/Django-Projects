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
    """if removepunc == "on":
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
        return HttpResponse('Error')"""


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


# doing some change hare
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        text = {'purpose': 'Remove punctations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', text)

    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        text={'purpose': 'Full Capitalyzed','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', text)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        text={'purpose': 'Extra space remover','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', text)
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed=analyzed+char
        text = {'purpose': 'Newline remover', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', text)
    if charcounter == "on":
        analyzed= 0
        for char in djtext:
            if char == " ":
                continue
            else:
                analyzed = analyzed+1
        text = {'purpose': 'Total character', 'analyzed_text': analyzed}
    if(removepunc!="on"and fullcaps !="on" and newlineremove !="on" and extraspaceremover !="on" and charcounter !="on"):
        return HttpResponse('''<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Home page</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Django</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact Us</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
    </nav>

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Error !</strong> You do not select anything. Please Try Again!!!!!!
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
    </script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
    </script>
</body>

</html>''')
    return render(request, 'analyze.html', text)
