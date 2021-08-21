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

