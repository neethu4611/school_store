from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)


            return redirect('college_app:reg')
        else:

            return redirect('credentials_app:login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confpassword = request.POST['confpassword']
        if(password==confpassword):
            if User.objects.filter(username=username).exists():
                messages.info(request, "* username already exist *")
                return redirect('credentials_app:register')

            else:

                user = User.objects.create_user(username=username, password=password)
                user.save();

                return redirect('credentials_app:login')

        else:
            messages.info(request, "*password not matching*")
            return redirect('credentials_app:register')


    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')



