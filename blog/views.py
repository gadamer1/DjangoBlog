from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify
# Create your views here.
#about
def about(request):
    return render(request,'blog/about/about.html',{})

#posts
def post_list(request):
    posts = Post.objects.all()
    p = posts.filter(category='POSTS').order_by('published_date').reverse()
    return render(request,'blog/posts/post_list.html',{'posts':p})

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
            instance.category = 'POSTS'
            instance.save()
            return redirect('blog:posts')
    else:
        form = forms.CreatePost()
    return render(request,'blog/posts/post_create.html',{'form':form})

@login_required(login_url='/userapp/login/')
def post_edit(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_404.html',{})
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES,instance=post)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.category = 'POSTS'
            instance.save()
            return redirect('blog:posts_detail')
    else:
        form = forms.CreatePost(instance=post)
    return render(request,'blog/posts/post_edit.html',{'form':form})
        

def post_delete(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_404.html')
    post.delete()
    return redirect('blog:posts')

#algorithm
def algorithm_list(request):
    posts = Post.objects.all()
    p = posts.filter(category='ALGORITHM').order_by('published_date').reverse()
    return render(request,'blog/algorithm/algorithm_list.html',{'posts':p})

def algorithm_detail(request,algorithm_slug):
    try:
        post = Post.objects.get(slug=algorithm_slug)
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
            instance.category = 'ALGORITHM'
            instance.save()
            return redirect('blog:algorithm')
    else:
        form = forms.CreatePost()
    return render(request,'blog/algorithm/algorithm_create.html',{'form':form})

#hacking
def hacking_list(request):
    posts = Post.objects.all()
    p = posts.filter(category='HACKING').order_by('published_date').reverse()
    return render(request,'blog/hacking/hacking_list.html',{'posts':p})

def hacking_detail(request,hacking_slug):
    try:
        post = Post.objects.get(slug=hacking_slug)
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
            instance.category = 'HACKING'
            instance.save()
            return redirect('blog:hacking')
    else:
        form = forms.CreatePost()
    return render(request,'blog/hacking/hacking_create.html',{'form':form})

#eating
def eating_list(request):
    posts = Post.objects.all()
    p = posts.filter(category='EATING').order_by('published_date').reverse()
    return render(request,'blog/eating/eating_list.html',{'posts':p})

def eating_detail(request,eating_slug):
    try:
        post = Post.objects.get(slug=eating_slug)
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
            instance.category = 'EATING'
            instance.save()
            return redirect('blog:eating')
    else:
        form = forms.CreatePost()
    return render(request,'blog/eating/eating_create.html',{'form':form})


#services
def services_list(request):
    posts = Post.objects.all()
    p = posts.filter(category='SERVICES').order_by('published_date').reverse()
    return render(request,'blog/services/services_list.html',{'posts':p})

def services_detail(request,eating_slug):
    try:
        post = Post.objects.get(slug=eating_slug)
    except Post.DoesNotExist:
        return render(request,'page_404.html',{})
    return render(request,'blog/services/services_content.html',{'post':post})

@login_required(login_url='/userapp/login/')
def services_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.category = 'SERVICES'
            instance.save()
            return redirect('blog:services')
    else:
        form = forms.CreatePost()
    return render(request,'blog/services/services_create.html',{'form':form})
