from projects.models import Project
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Project

# Create your views here.
def projects(request):
    projectList = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projectList})

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':projectObject})
