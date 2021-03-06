from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return redirect('blog:about')
    else:
        form = AuthenticationForm()
    return render(request,'userapp/login.html',{'form':form})



def logout_view(request):
    logout(request)
    return render(request,'blog/about/about.html')

