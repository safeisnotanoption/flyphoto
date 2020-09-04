from PIL import Image
from django import forms
from django.core.files import File
from .models import Project, Photo
from django.forms import ModelForm, Textarea, TextInput


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
