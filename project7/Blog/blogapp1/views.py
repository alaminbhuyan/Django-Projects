from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def blog(request):
    allPost = Post.objects.all()
    #print(allPost)
    context = {'allPost': allPost}
    return render(request, 'blogapp1/blogHome.html',context)

def blogpost(request , slug):
    # return HttpResponse(f"hi this is blog post.{slug}")
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'blogapp1/blogPost.html',context)
