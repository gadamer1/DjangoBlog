from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse

# Create your views here.
#about
def about(request):
    return render(request,'blog/about/about.html',{})

#posts
def post_list(request):
    page = request.GET.get('page','1')
    page = int(page)
    posts = Post.objects.filter(category='POSTS').order_by('created_date').reverse()
    num=5

    paginator = Paginator(posts,num)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5
    
    page_range = range(start_index,end_index+1)
    return render(request, 'blog/posts/post_list.html', {'posts': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})

def post_detail(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
    return render(request,'blog/posts/post_content.html',{'post':post})

@login_required(login_url='/userapp/login/')
def post_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            #slug(title) must be unique
            instance.my_slugify()
            instance.category= 'POSTS'
            try:
                post = Post.objects.get(category='POSTS' ,slug = instance.slug)
                messages.warning(request,'Please check your title is unique')
            except Post.DoesNotExist:
                instance.author = request.user
                instance.publish()
                return redirect('blog:post_detail',instance.slug)
    else:
        form = forms.CreatePost()
    return render(request,'blog/posts/post_create.html',{'form':form})

@login_required(login_url='/userapp/login/')
def post_edit(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
        if request.method == "POST":
            form = forms.CreatePost(request.POST, request.FILES,instance=post)
            if form.is_valid():
                #save post to db
                instance = form.save(commit = False)
                instance.my_slugify()
                instance.publish()
                messages.success(request,'post updated')
                return redirect('blog:post_detail',instance.slug)
        else:
            form = forms.CreatePost(instance=post)
        return render(request,'blog/posts/post_edit.html',{'form':form, 'post':post})

    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
        

def post_delete(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
    post.delete()
    return redirect('blog:posts')

#algorithm
def algorithm_list(request):
    page = request.GET.get('page','1')
    page = int(page)
    posts = Post.objects.filter(category='ALGORITHM').order_by('created_date').reverse()
    num=5

    paginator = Paginator(posts,num)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5

    page_range = range(start_index,end_index+1)
    return render(request, 'blog/algorithm/algorithm_list.html', {'posts': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})

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
            #slug(title) must be unique
            instance.category = 'ALGORITHM'
            instance.my_slugify()
            try:
                post = Post.objects.get(category='ALGORITHM', slug = instance.slug)
                messages.warning(request,'Please check your title is unique')
            except Post.DoesNotExist:
                instance.author = request.user
                instance.publish()
                redirect('blog:eating_datail',instance.slug)
    else:
        form = forms.CreatePost()
    return render(request,'blog/algorithm/algorithm_create.html',{'form':form})


@login_required(login_url='/userapp/login/')
def algorithm_edit(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
        if request.method == "POST":
            form = forms.CreatePost(request.POST, request.FILES,instance=post)
            if form.is_valid():
                #save post to db
                instance = form.save(commit = False)
                instance.my_slugify()
                instance.publish()
                messages.success(request,'post updated')
                return redirect('blog:algorithm_detail',instance.slug)
        else:
            form = forms.CreatePost(instance=post)
        return render(request,'blog/algorithm/algorithm_edit.html',{'form':form, 'post':post})

    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
        
def algorithm_delete(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
    post.delete()
    return redirect('blog:algorithm')

#hacking
def hacking_list(request):
    page = request.GET.get('page','1')
    page = int(page)
    posts = Post.objects.filter(category='HACKING').order_by('created_date').reverse()
    num=5

    paginator = Paginator(posts,num)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5

    page_range = range(start_index,end_index+1)
    return render(request, 'blog/hacking/hacking_list.html', {'posts': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})

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
            #slug(title) must be unique
            instance.my_slugify()
            instance.category = 'HACKING'
            try:
                post = Post.objects.get(category = 'HACKING', slug = instance.slug)
                messages.warning(request,'Please check your title is unique')
            except Post.DoesNotExist:
                instance.author = request.user
                instance.publish()
                return redirect('blog:hacking_detail',instance.slug)
    else:
        form = forms.CreatePost()
    return render(request,'blog/hacking/hacking_create.html',{'form':form})

@login_required(login_url='/userapp/login/')
def hacking_edit(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
        if request.method == "POST":
            form = forms.CreatePost(request.POST, request.FILES,instance=post)
            if form.is_valid():
                #save post to db
                instance = form.save(commit = False)
                instance.my_slugify()
                instance.publish()
                messages.success(request,'post updated')
                return redirect('blog:hacking_detail',instance.slug)
        else:
            form = forms.CreatePost(instance=post)
        return render(request,'blog/hacking/hacking_edit.html',{'form':form, 'post':post})

    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
        
def hacking_delete(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
    post.delete()
    return redirect('blog:hacking')

#eating
def eating_list(request):
    page = request.GET.get('page','1')
    page = int(page)
    posts = Post.objects.filter(category='EATING').order_by('created_date').reverse()
    num=5

    paginator = Paginator(posts,num)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5

    page_range = range(start_index,end_index+1)
    return render(request, 'blog/eating/eating_list.html', {'posts': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})

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
            #slug(title) must be unique
            instance.my_slugify()
            instance.category='EATING'
            try:
                post = Post.objects.get(category='EATING',slug = instance.slug)
                messages.warning(request,'Please check your title is unique')
            except Post.DoesNotExist:
                instance.author = request.user
                instance.publish()
                return redirect('blog:eating_detail',instance.slug)
    else:
        form = forms.CreatePost()
    return render(request,'blog/eating/eating_create.html',{'form':form})

@login_required(login_url='/userapp/login/')
def eating_edit(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
        if request.method == "POST":
            form = forms.CreatePost(request.POST, request.FILES,instance=post)
            if form.is_valid():
                #save post to db
                instance = form.save(commit = False)
                instance.my_slugify()
                instance.publish()
                messages.success(request,'post updated')
                return redirect('blog:eating_detail',instance.slug)
        else:
            form = forms.CreatePost(instance=post)
        return render(request,'blog/eating/eating_edit.html',{'form':form, 'post':post})

    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
        
def eating_delete(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
    post.delete()
    return redirect('blog:eating')


#services
def services_list(request):
    page = request.GET.get('page','1')
    page = int(page)
    posts = Post.objects.filter(category='SERVICES').order_by('created_date').reverse()
    num=5

    paginator = Paginator(posts,num)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    #if page's number smaller than 5
    if paginator.num_pages < num:
        num= paginator.num_pages
    
    start_index = 1
    end_index = paginator.num_pages
    if p.number>5:
        start_index = p.number-5
    if paginator.num_pages > p.number+5:
        end_index = p.number+5

    page_range = range(start_index,end_index+1)
    return render(request, 'blog/services/services_list.html', {'posts': p, 'page_range': page_range,
    'page_start_index':start_index,'page_end_index':end_index})


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
            #slug(title) must be unique
            instance.my_slugify()
            instance.category = 'SERVICES'
            try:
                post = Post.objects.get(category='SERVICES' ,slug = instance.slug)
                messages.warning(request,'Please check your title is unique')
            except Post.DoesNotExist:
                instance.author = request.user
                instance.publish()
                return redirect('blog:services_detail',instance.slug)
    else:
        form = forms.CreatePost()
    return render(request,'blog/services/services_create.html',{'form':form})

@login_required(login_url='/userapp/login/')
def services_edit(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
        if request.method == "POST":
            form = forms.CreatePost(request.POST, request.FILES,instance=post)
            if form.is_valid():
                #save post to db
                instance = form.save(commit = False)
                instance.my_slugify()
                instance.publish()
                messages.success(request,'post updated')
                return redirect('blog:services_detail',instance.slug)
        else:
            form = forms.CreatePost(instance=post)
        return render(request,'blog/services/services_edit.html',{'form':form, 'post':post})

    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
        
def services_delete(request,post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return render(request,'blog/page_error/page_404.html')
    post.delete()
    return redirect('blog:services')

