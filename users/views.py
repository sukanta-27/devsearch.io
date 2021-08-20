from django.http import request
from django.shortcuts import render

# Create your views here.
def profiles(request):
    return render(request=request, template_name='users/profiles.html')

