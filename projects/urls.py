from django.urls import path
from .views import project, projects, \
    createProject, updateProject, deleteProject

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', createProject, name='create-project'),
    path('update-project/', updateProject, name='update-project'),
    path('delete-project/', deleteProject, name='delete-project'),
]