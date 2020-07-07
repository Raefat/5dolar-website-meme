from django.shortcuts import render
from mysecApp.models import User
from django.http import HttpResponse


# Create your views here.

def users(request):
    users = User.objects.order_by('first_name')
    my_dict = {
        'users': users,
    }
    return render(request,'second-app/users.html',context=my_dict)
