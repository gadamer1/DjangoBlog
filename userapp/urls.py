from django.urls import path
from . import views

urlpatterns = [
    path('user_auth/',views.user_auth,name ='user_auth'),
]