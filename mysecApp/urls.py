from django.urls import path
from mysecApp import views

#app_name = 'users'

urlpatterns = [
    path('users',views.users,name='users'),
]
