from django.http import request
from django.shortcuts import render
from .models import Profile

# Create your views here.
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
