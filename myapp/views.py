from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import now

def home(request):
     return render(request, "home.html", {})

def currentdate(request):
     current_time = now()
     return render(request, "currentdate.html", {})

def about(request):
     return render(request, "about.html")

def services(request):
     return render(request, "services.html")

def alarm(request):
     return render(request, "alarm.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful!")
                return redirect("login")  # Change this to your login URL
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "register.html")




