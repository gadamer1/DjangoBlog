from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
#about
def about(request):
    return render(request,'blog/about/about.html',{})

#posts
def post_list(request):
    posts = Post.objects.all().order_by('published_date').reverse()
    return render(request,'blog/posts/post_list.html',{'posts':posts})

def post_detail(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'page_404.html',{})
    return render(request,'blog/posts/post_content.html',{'post':post})

@login_required(login_url='/userapp/login/')
def post_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:posts')
    else:
        form = forms.CreatePost()
    return render(request,'blog/posts/post_create.html',{'form':form})

#algorithm
def algorithm_list(request):
    posts = Post.objects.all().order_by('published_date').reverse()
    return render(request,'blog/algorithm/algorithm_list.html',{'posts':posts})

def algorithm_detail(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'page_404.html',{})
    return render(request,'blog/algorithm/algorithm_content.html',{'post':post})

@login_required(login_url='/userapp/login/')
def algorithm_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:algorithm')
    else:
        form = forms.CreatePost()
    return render(request,'blog/algorithm/algorithm_create.html',{'form':form})

#hacking
def hacking_list(request):
    posts = Post.objects.all().order_by('published_date').reverse()
    return render(request,'blog/hacking/hacking_list.html',{'posts':posts})

def hacking_detail(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'page_404.html',{})
    return render(request,'blog/hacking/hacking_content.html',{'post':post})

@login_required(login_url='/userapp/login/')
def hacking_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:hacking')
    else:
        form = forms.CreatePost()
    return render(request,'blog/hacking/hacking_create.html',{'form':form})

#eating
def eating_list(request):
    posts = Post.objects.all().order_by('published_date').reverse()
    return render(request,'blog/eating/eating_list.html',{'posts':posts})

def eating_detail(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'page_404.html',{})
    return render(request,'blog/eating/eating_content.html',{'post':post})

@login_required(login_url='/userapp/login/')
def eating_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:eating')
    else:
        form = forms.CreatePost()
    return render(request,'blog/eating/eating_create.html',{'form':form})
