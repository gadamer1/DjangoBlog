from django.urls import path
from . import views
from django.contrib.auth.views import logout
app_name='userapp'

urlpatterns = [
    path('',views.login_view,name ='login'),
    path('logout/',logout,name='logout'),
]