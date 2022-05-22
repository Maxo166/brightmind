from django.contrib import messages
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from . import models
# Create your views here.


def index(request):
    courses = models.Course.objects.all()
    return render(request, 'main/index.html', {'courses': courses})


def signup(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'new comment is added successfuly')
            return redirect("/index")
        else:
            messages.error(request, "invalid form")
    else:
        form = forms.RegisterForm()
    return render(request, 'registration/signup.html', {'signup_form': form})
