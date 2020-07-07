"""frst_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from myApp import views
from mysecApp import views as views_2
from mythirdApp import views as views_3

urlpatterns = [
    path('',views.index,name='index'),
    path('pp/',views.about,name='about'),
    path('users/', views_2.users,name='users'), #),include('mysecApp.urls')
    path('forms/', views_3.forms,name='forms'),
    path('formodel/',views_3.formodel,name='formodel'),
    path('fileupload/',views_3.uploadform,name='fileupload'),
    path('logout/', views_3.user_logout,name='logout'),
    path('special/', views_3.special,name='special'),
    path('login/', views_3.user_login,name='login'),
    path('admin/', admin.site.urls),
    #views_3.uploadform,name='uploadform'
]
