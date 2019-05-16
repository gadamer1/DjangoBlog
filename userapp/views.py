from django.shortcuts import render

# Create your views here.


def user_auth(request):
    return render(request,'user_auth.html',{})