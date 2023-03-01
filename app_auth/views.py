from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def login_blog(request):
    if request.method =="POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        print('username:',username)
        user = authenticate(username = username, password = pwd)
        if user is not None:
            return redirect("essai")
        else:
            messages.error(request,"erreur d'authantentification")
            return render (request,'login.html')
    
    return render(request,"login.html")