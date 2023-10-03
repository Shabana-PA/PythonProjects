from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "customer.html")  # Redirect to the home page or another appropriate view
        else:
            messages.error(request, "Invalid credentials")
            return redirect(reverse('credentials:login'))  # Fix the parenthesis mismatch

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect(reverse('credentials:login'))
            except IntegrityError:
                messages.error(request, "An error occurred during registration.")
                return redirect('credentials:register')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('credentials:register')  # Redirect to the registration page
    else:
        # Handle GET requests if needed
        return render(request, "register.html")


# credentials/views.py

@login_required
def logout(request):
    auth.logout(request)
    return redirect('credentials:login')