from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginpage(request):
    next = request.GET.get('next')
    print(next)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,"login.html")

@csrf_exempt
def submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    User.objects.create_user(username=username,email=username,password=password,first_name=first_name,last_name=last_name)
    return HttpResponse("<h1>User successfully registered</h1>")

@csrf_exempt
def signin(request):
    next = "something"
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    user = authenticate(request, username=username, password=password)

    if user is not None:
        if next is not None:
            return redirect(next)
        else:
            return redirect('home')
    else:
        return redirect('login')

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        return redirect('login')

def signout(request):
    logout(request)
    return redirect('login')


def demo(request):
    return render(request,"demo.html")