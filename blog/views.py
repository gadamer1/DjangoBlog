from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    return render(request,'blog/home_page.html',{})

def post_list(request):
    posts = Post.objects.all().order_by('published_date').reverse()
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'page_404.html',{})
    return render(request,'blog/post_content.html',{'post':post})