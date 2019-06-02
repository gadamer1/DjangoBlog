from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    #about
    path('about/', views.about,name ='about'),
    #posts
    path('post/',views.post_list, name= 'posts'),
    path('post/<slug:post_slug>/',views.post_detail,name='post_detail'),
    path('create/posts/',views.post_create,name='post_create'),
    path('post/<slug:post_slug>/edit/',views.post_edit, name='post_edit'),
    path('post/<slug:post_slug>/delete/',views.post_delete, name='post_delete'),

    #algorithm
    path('algorithm/',views.algorithm_list, name= 'algorithm'),
    path('algorithm/<slug:algorithm_slug>/',views.algorithm_detail,name='algorithm_detail'),
    path('create/algorithm/',views.algorithm_create,name='algorithm_create'),
    path('algorithm/<slug:post_slug>/edit/',views.algorithm_edit, name='algorithm_edit'),
    path('algorithm/<slug:post_slug>/delete/',views.algorithm_delete, name='algorithm_delete'),
    #hacking
    path('hacking/',views.hacking_list, name= 'hacking'),
    path('hacking/<slug:hacking_slug>/',views.hacking_detail,name='hacking_detail'),
    path('create/hacking/',views.hacking_create,name='hacking_create'),
    path('hacking/<slug:post_slug>/edit/',views.hacking_create, name='hacking_edit'),
    path('hacking/<slug:post_slug>/delete/',views.hacking_delete, name='hacking_delete'),
    #eating
    path('eating/',views.eating_list, name= 'eating'),
    path('eating/<slug:eating_slug>/',views.eating_detail,name='eating_detail'),
    path('create/eating/',views.eating_create,name='eating_create'),
    path('eating/<slug:post_slug>/edit/',views.eating_edit, name='eating_edit'),
    path('eating/<slug:post_slug>/delete/',views.eating_delete, name='eating_delete'),
    #services
    path('services/',views.services_list, name= 'services'),
    path('services/<slug:eating_slug>/',views.services_detail,name='services_detail'),
    path('create/services',views.services_create,name='services_create'),
    path('services/<slug:post_slug>/edit/',views.services_edit, name='services_edit'),
    path('services/<slug:post_slug>/delete/',views.services_delete, name='services_delete'),
]
