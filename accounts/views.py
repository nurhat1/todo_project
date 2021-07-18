from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_view(request):
    """
    Log in the user via email
    """
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            return redirect("task_list")
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)

    return redirect("login")
