from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image',\
             'demo_link', 'source_link', 'tags']