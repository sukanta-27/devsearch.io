from projects.models import Project
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projectList = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projectList})

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':projectObject})

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form,
    }    
    return render(request, 'projects/project-form.html', context)

@login_required(login_url='login')
def updateProject(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form,
    }    
    return render(request, 'projects/project-form.html', context)

@login_required(login_url='login')
def deleteProject(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    context = {'object': project}
    return render(request, 'projects/delete-template.html', context)


