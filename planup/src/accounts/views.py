from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm

@login_required
def home(request):
    return render(request, 'home.html')

def login_view(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            registration = form.cleaned_data.get("username")
            print(registration)
            password = form.cleaned_data.get("password")
            print(password)
            user = authenticate(username=registration, password=password)
            login(request,user)
            return redirect("home")

    else:

        form = LoginForm()
    return render(request, "login.html", {"form": form})


