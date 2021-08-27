from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
import logging

logging.basicConfig(level=logging.DEBUG)

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            logging.error("User does not exist in the database")
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        login(request, user)

        return redirect('profiles')

    return render(request, 'users/login-registration.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

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
