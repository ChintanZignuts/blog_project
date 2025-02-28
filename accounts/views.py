from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm
from django.contrib import messages

# User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after successful registration
            return redirect("blog_list")  # Redirect to the blog list page
    else:
        form = RegisterForm()
    
    return render(request, "accounts/register.html", {"form": form})

# User Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog_list")  
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect("blog_list")