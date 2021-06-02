from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import my_registration_form, my_login_form


# Create your views here.


def registration_view(req, *args, **kwargs):
    context = {}
    if req.POST:
        form = my_registration_form(req.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(req, email=email, password=password)
            login(req, user)
            return redirect("home")
        else:
            context["registration_form"] = form
            context["error"] = "The following Email ID is already registered!"
    else:
        form = my_registration_form()
        context["registration_form"] = form
    return render(req, "register.html", context)


def login_view(req, *args, **kwargs):
    context = {}
    if req.POST:
        form = my_login_form(req.POST)
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, email=username, password=password)
        if user != None:
            login(req, user)
            return redirect("home")
        else:
            context["login_form"] = form
            context["error"] = "The Email ID or Password is incorrect!"
    else:
        form = my_login_form()
        context["login_form"] = form
    return render(req, "login.html", context)


def logout_view(req, *args, **kwargs):
    logout(req)
    return redirect("home")


def profile_view(request, *args, **kwargs):
    return render(request, "profile.html")
