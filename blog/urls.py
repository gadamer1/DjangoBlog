from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.home,name ='home'),
    path('post/',views.post_list, name= 'list'),
    path('post/<slug:post_slug>/',views.post_detail,name='detail')
]
