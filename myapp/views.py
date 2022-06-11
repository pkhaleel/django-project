
from django.shortcuts import redirect, render
from flask import url_for

from .models import Student 

from .forms import Studentform

from django.contrib import messages

from django.contrib.auth.models import User,auth

# Create your views here.

def dashboard(request):

    student=Student.objects.all 

    form=Studentform

    return render(request,"dashboard.html",{'student':student,'form':form})

def add(request):
    form=Studentform(request.POST)

    form.save()

    return redirect('dashboard')


def edit(request,id):
    student=Student.objects.get(id=id)

    return render(request,"edit.html",{'student':student})

def update(request,id):
     student=Student.objects.get(id=id)

     form=Studentform(request.POST,instance=student)

     form.save()

     return redirect('dashboard')


def delete(request,id):

    student=Student.objects.get(id=id)

    student.delete()

    return redirect('dashboard')



def home(request):

    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        cpassword=request.POST['password2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email id already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                user.save()
                return redirect('/')
        else:
            messages.info(request,"passwords not matching")
            return redirect('register')
    return render(request,"register.html")



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"invalid credentials")

    return render(request,"login.html")

def logout(request):

    auth.logout(request)

    return redirect('/')