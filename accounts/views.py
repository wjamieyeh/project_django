from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . forms import SignUpForm
from django.contrib import auth

def signup(request):
    registered = False

    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        signup_form = SignUpForm()

    return render(request, 'signup.html', {
    'title': 'Welcome to the Home Page',
    'signup_form': signup_form,
    'registered': registered,
    })

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
        username = request.POST['username'],
        password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
            'title': 'Something went wrong',
            'error': 'Username or Password Invalid'
            })

    return render(request, 'login.html', {'title': 'Please login'})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
