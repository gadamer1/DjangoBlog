from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponse
# Create your views here.

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request,'userapp/login.html',{'form':form})

    elif request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('blog:home')
        else:
            return render(request,'userapp/login.html',{'forms':form})
    else:
        form = AuthenticationForm()
        return render(request,'userapp/login.hmtl',{'form':form})
