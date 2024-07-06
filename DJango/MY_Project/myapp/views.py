from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # return render(request,'success.html')
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username,email,password)
                user.save()
                return redirect('Login')
        else:
            messages.info(request,'Password mismatched')
            return redirect('register')
    else:
        return render(request,'register.html')

def upload_doc(request):
    content = request._post['content']
    lenght = len(content)
    return render(request,'upload.html',{"Length":lenght})

from django.contrib import auth, messages
from django.shortcuts import redirect, render

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}, Password: {password}")  # Debug statement
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/land')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/land')

def counter(request):
    posts = [1,2,3,4,5,'teja','vardhan','reddy','cr']
    return render (request,'counter.html',{'posts':posts})

def posts(request,pk):
    return render(request,'post.html',{'pk':pk})