from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home,name ='home'),
    path('post/',views.post_list, name= 'list'),
    path('post/<slug:post_slug>/',views.post_detail,name='detail'),
]
