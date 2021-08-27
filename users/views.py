from django.contrib.messages.api import info
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm
import logging

logging.basicConfig(level=logging.DEBUG)

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            logging.error("User does not exist in the database")
            messages.add_message(request, messages.WARNING, "User does not exist in the database")
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            logging.error("Username or Password is incorrect")
            messages.add_message(request, messages.WARNING, "Username or Password is incorrect")

    page = 'login'
    context = {
        'page': page,
    }
    return render(request, 'users/login-registration.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()


            login(request, user)
            logging.info("User created Successfully!")
            messages.success(request, "User created Successfully!")
            return redirect("profiles")
        else:
            logging.info("An error occurred while creating the user")
            messages.error(request, "An error occurred while creating the user")

    context = {
        'page': page,
        "form": form,
    }

    return render(request, 'users/login-registration.html', context)
    

def profiles(request):
    profileList = Profile.objects.all()
    context = {
        'profiles': profileList,
    }
    return render(request=request, \
        template_name='users/profiles.html', context=context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
    }
    return render(request, 'users/user-profile.html', context)
