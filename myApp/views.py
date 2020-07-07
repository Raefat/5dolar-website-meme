from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Topic,AccessRecord,Webpage

# Create your views here.

def index(request):
    #return HttpResponse("HELLO WORLD *myApp*")
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {'insert_me': webpages_list}
    return render(request,'first-app/index.html',context=my_dict)

def about(request):
    return HttpResponse("<h1>SUCK IT LOSER </h1>")
