from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mythirdApp.forms import FormName ,MahForm ,UserProfileInfoForm ,UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import login,logout,authenticate

# Create your views here.

def forms(request):
    my_data = FormName()

    if request.method == 'POST':
        my_data = FormName(request.POST)
        if my_data.is_valid():
            print("VALIDATION SUCCESS!!")
            print("name  :", my_data.cleaned_data['name'])
            print("email :" ,my_data.cleaned_data['email'])
            print("text :" ,my_data.cleaned_data['text'])

    my_dict = {'data' : my_data}
    return render(request,'third-app/forms.html',context=my_dict)


def formodel(request):
    my_form = MahForm()
    if request.method == 'POST':
        my_form = MahForm(request.POST)
        if my_form.is_valid():
            my_form.save(commit=True)
            return render(request,'second-app/users.html')
        else :
            print("Something is freaking wrong here ^^")
    return render(request,'third-app/forms-model.html',{'my_form':my_form})

def uploadform(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        upload_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and upload_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = upload_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered =True
        else:
            print(user_form.errors, upload_form.errors)
    else:
        user_form = UserForm()
        upload_form = UserProfileInfoForm()
    return render(request,'third-app/file-upload.html',{'upload_form':upload_form,'user_form':user_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('<h1>BUHAHA You Are Not An Active User !</h1>')
        else:
            print("This User Has Failed To Login : ",username, "/n His Pass Is :",password)
            return HttpResponse('<h1>Invalid Login</h1>')
    else:
        return render(request,'third-app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
@login_required
def special(request):
    return HttpResponse('You Are logged in')

