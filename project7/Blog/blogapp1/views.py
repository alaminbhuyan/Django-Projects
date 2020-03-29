from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render(request, 'blogapp1/blogHome.html')

def blogpost(request , slug):
    # return HttpResponse(f"hi this is blog post.{slug}")
    return render(request, 'blogapp1/blogPost.html')
